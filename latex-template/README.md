# EdUHK Robotics LaTeX Template

这是 EdUHK Robotics Team 的 A4 技术文档模板。它沿用本仓库的深绿色品牌色、横版队徽、TeX Live 自带的无衬线字体、信息卡片、表格和浅蓝色代码块，适合技术报告、设计记录与比赛文档。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `eduhk_robotics_template.tex` | XeLaTeX 模板与完整示例文档 |
| `enc_imu_may31.ino` | Robocon 2026 EdUHK Robotics Team R2 的 Arduino IMU 与编码器接收程序，作者 Steven Zhang Yancheng |
| `preview.pdf` | 模板编译后的预览 |

## 示例代码来源

`enc_imu_may31.ino` 来源于 `Robocon2026_r2` 仓库的 `dev` 分支：

[Steven-ZYC/Robocon2026_r2 - enc_imu_may31.ino](https://github.com/Steven-ZYC/Robocon2026_r2/blob/dev/2026R2_ws/src/arduino_sensor_driver/docs/enc_imu_may31.ino)

模板与预览 PDF 中均保留了此来源链接，并注明该程序用于 Robocon 2026 EdUHK Robotics Team R2，作者为 Steven Zhang Yancheng。

## 编译

请从本目录运行 XeLaTeX；编译两次可以正确生成总页数。

```powershell
cd latex-template
xelatex -interaction=nonstopmode -halt-on-error eduhk_robotics_template.tex
xelatex -interaction=nonstopmode -halt-on-error eduhk_robotics_template.tex
```

模板会优先读取本仓库的 `../logos/team-logo.png`，也支持从仓库根目录编译时使用 `logos/team-logo.png`。代码示例同样支持从本目录或仓库根目录读取。

模板正文使用 TeX Live 自带字体。为完整显示示例源码中的简繁中文注释，代码区会优先使用 `Noto Sans CJK SC`，Windows 下也可自动使用 Microsoft YaHei；两者均不可用时回退到 Fandol 字体。

## 自定义文档

1. 修改文件顶部的 `DocumentTitle`、`DocumentSubtitle`、`DocumentAuthor`、`DocumentDate` 和 `DocumentVersion`。
2. 保留或删除示例章节，并使用 `infobox`、`neutralbox`、`tabularx` 和 `lstlisting` 组件编写内容。
3. 如需引用外部源码，可仿照 `CodeExampleFile` 与 `lstinputlisting` 的写法。

代码示例在文档中明确标注为：**Robocon 2026 EdUHK Robotics Team R2 Arduino IMU and encoder receiver program — by Steven Zhang Yancheng**。
