"""Add a Week 6 style tiled watermark. Requires: pip install pypdf reportlab.
Usage: python watermark_week7.py [input.pdf] [output.pdf]
"""
import io
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


def watermark(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('Input and output must be different files')
    reader = PdfReader(source)
    writer = PdfWriter()
    for page in reader.pages:
        w, h = float(page.mediabox.width), float(page.mediabox.height)
        stream = io.BytesIO()
        c = canvas.Canvas(stream, pagesize=(w, h))
        c.setFillColorRGB(0.65, 0.65, 0.65)
        c.setFillAlpha(0.16)
        c.setFont('Helvetica-Bold', w * 0.020)
        # Fixed spacing in one rotated coordinate system (no alternating offsets).
        # At 900px page width: column pitch 280px, perpendicular row pitch 72px.
        column_pitch = w * (280 / 900)
        row_pitch = w * (72 / 900)
        c.saveState()
        c.translate(w / 2, h / 2)
        c.rotate(30)
        extent = (w * w + h * h) ** 0.5
        nx = int(extent / column_pitch) + 2
        ny = int(extent / row_pitch) + 2
        for row in range(-ny, ny + 1):
            for col in range(-nx, nx + 1):
                c.drawString(col * column_pitch, row * row_pitch,
                             'EdUHK Robocon Team 2027')
        c.restoreState()
        c.save()
        stream.seek(0)
        page.merge_page(PdfReader(stream).pages[0])
        writer.add_page(page)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('wb') as f:
        writer.write(f)
    print(f'Watermarked {len(reader.pages)} pages: {destination}')


if __name__ == '__main__':
    watermark(sys.argv[1] if len(sys.argv) > 1 else Path.home() / 'Downloads/RC27-week7-Steven.pdf',
              sys.argv[2] if len(sys.argv) > 2 else Path(__file__).with_name('RC27-week7-Steven-watermarked.pdf'))
