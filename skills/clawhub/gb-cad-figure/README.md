# gb-cad-figure · 国标·CAD·图形

**gb-cad-figure = GB(中国国标) + CAD(计算机辅助设计) + figure(图形/图幅)**

一套按中国国家标准 **GB/T** 自动生成正式工程图纸与 CAD 文件的开源工具/技能：从实体图元（平滑回转体 lathe / 圆柱 cyl / 立方体 box）自动选图幅、排图框、生成标题栏、国标尺寸标注、技术说明与图例，并交付 **PDF + DXF + DWG** 三种格式。

## Features
- GB/T 标准图幅（A0~A4）**自动选幅 + 标准比例**
- 图框 / 标题栏（外框四边完整、图名大格醒目、格网紧凑）/ 图例 / 技术说明 全参数化自适应布局
- **平滑回转体（lathe）**等轴测 · 点画中心线贯穿 · 瓶底拱形前缘 · **引线式标注（LDIMS）不穿实体**
- 中文字体防方块；出图自动自检（字体 / 线连接闭合 / 遮挡 / 布局不贴框）
- **三格式交付**：PDF（查看/打印）+ DXF + DWG（ODA File Converter + Xvfb 转换，默认 ACAD2018）

## Quick Start
```bash
# 1) 生成图纸 → 引擎主脚本（Python，ezdxf + reportlab + fitz）
python3 scripts/gb_figure.py

# 2) 校验 DXF 中文字体(防方块)
python3 scripts/check_dxf_fonts.py 输出.dxf

# 3) 单个 DXF 转 DWG（首次运行自动下载 ODA 转换器）
bash scripts/dxf2dwg.sh 输入.dxf 输出目录/
```

## DWG 转换依赖
仅出 PDF/DXF 无需额外依赖。需要 DWG 时，`dxf2dwg.sh` 会自动调用 `scripts/tools/fetch_oda.sh` **下载 ODA File Converter**（Autodesk 官方免费 AppImage，约 82MB）到 `scripts/tools/`，再经系统 `xvfb-run` 批量转换（默认 ACAD2018，可指定 ACAD2000~2021）。

> ClawHub 单文件限 10MB，因此 82MB 转换器**不打包进技能**，改为首次转 DWG 时自动拉取。也可手动放 `scripts/tools/ODAFileConverter.AppImage` 或设环境变量 `ODA_IMG=路径` 跳过下载。

## Keywords / GitHub Topics
`gb` `cad` `figure` `engineering-drawing` `autocad` `isometric` `dimension` `titleblock` `dxf` `dwg`
`国标` `工程图` `机械制图` `建筑制图` `CAD图纸` `等轴测` `尺寸标注` `图框` `标题栏`

## 目录结构
```
scripts/
  gb_figure.py          # 引擎：生成 PDF + DXF（自动选幅/标题栏/标注/中心线/拱形底/回转体）
  check_dxf_fonts.py    # 中文字体验证
  dxf2dwg.sh            # DXF→DWG 转换（首次自动下载 ODA + xvfb-run）
  tools/fetch_oda.sh    # 自动下载 ODAFileConverter.AppImage(~82MB)
```

## Tech Stack
- Python 3 · [ezdxf](https://ezdxf.mozman.at/)（DXF）· ReportLab（PDF）· ODA File Converter（DWG）

## License
MIT（开源建议）
