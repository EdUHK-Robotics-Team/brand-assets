# PDF Watermark Utility

Adds a diagonal, tiled text watermark to existing PDF documents, matching the Week 6-style watermark used in EdUHK Robotics Team training materials.

## Requirements

- Python 3
- [pypdf](https://pypi.org/project/pypdf/)
- [reportlab](https://pypi.org/project/reportlab/)

Install dependencies:

```bash
python -m pip install pypdf reportlab
```

## Usage

From the repository root:

```bash
python pdf-watermark/watermark_week7.py input.pdf output-watermarked.pdf
```

Example for Week 7:

```bash
python pdf-watermark/watermark_week7.py RC27-week7-Steven.pdf RC27-week7-Steven-watermarked.pdf
```

Both arguments are optional. By default, the script reads `~/Downloads/RC27-week7-Steven.pdf` and writes `RC27-week7-Steven-watermarked.pdf` to the folder containing the script. **Use different input and output paths**.

## Watermark style

- Text: `EdUHK Robocon Team 2027`
- Font: Helvetica Bold
- Rotation: 30°
- Colour: light grey
- Opacity: 16%
- Evenly spaced repeated pattern without alternating row offsets

The font size and spacing scale with page width. Each page is processed using its own dimensions.

To customize the watermark text, rotation, opacity, or spacing, edit the corresponding values in `watermark_week7.py`.

> This is a visible watermark, not a security control. It does not prevent editing, copying, or removing PDF content.
