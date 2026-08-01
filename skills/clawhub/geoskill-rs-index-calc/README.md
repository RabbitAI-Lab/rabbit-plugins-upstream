# Remote Sensing Index Calculator · 遥感指数计算器

> 输入 GeoTIFF 影像路径 + 指数名，自动计算并输出。
> 支持 **NDVI / NDBI / NDWI / EVI / SAVI / MNDWI / AWEI / NBR / BSI / UI**。
> **零依赖**（仅使用 Python 标准库）。
> MIT-0 开源。

[English](#quickstart) | 中文

## 为什么做这个

遥感指数（NDVI、NDBI 等）是遥感分析的基础操作。通常需要
Python + numpy + rasterio 或 ENVI/ArcGIS。本工具纯 Python 实现，
一条命令即可计算任意指数，适合批处理和脚本集成。


## Installation

### Cross-platform (skills.sh · 50+ AI agents)

```bash
npx skills add ruiduobao/rs-index-calc -g
```

Works with: Claude Code, Cursor, Codex, GitHub Copilot, Windsurf, Gemini CLI, Cline, AMP, VS Code, Zed, OpenClaw, and more.

### Claude Code (plugin marketplace)

```bash
/plugin marketplace add ruiduobao/claude-plugins
/plugin install rs-index-calc@ruiduobao-geo-skills
```

### ClawHub (OpenClaw)

```bash
clawhub install ruiduobao/rs-index-calc
```

### Manual

```bash
git clone https://github.com/ruiduobao/rs-index-calc.git
```

## Quickstart / 快速开始

```bash
# 零依赖，无需安装任何第三方库

# 计算 NDVI
python rs-index-calc.py input.tif --index ndvi --output ndvi.tif

# 计算多个指数
python rs-index-calc.py input.tif --index ndvi ndbi ndwi --output ./indices/

# 批量模式（计算所有支持的指数）
python rs-index-calc.py input.tif --batch --output ./indices/

# 自定义公式
python rs-index-calc.py input.tif --formula "(B4-B3)/(B4+B3)" --output custom.tif

# 指定波段顺序
python rs-index-calc.py input.tif --index ndvi \
    --bands red nir green blue swir1 swir2 \
    --output ndvi.tif
```

## 支持的指数 / Supported Indices

| 指数 | 全名 | 公式 | 应用 |
|---|---|---|---|
| **NDVI** | 归一化植被指数 | (NIR-Red)/(NIR+Red) | 植被监测 |
| **NDBI** | 归一化建筑指数 | (SWIR-NIR)/(SWIR+NIR) | 城市提取 |
| **NDWI** | 归一化水体指数 | (Green-NIR)/(Green+NIR) | 水体提取 |
| **EVI** | 增强植被指数 | 2.5×(NIR-Red)/(NIR+6×Red-7.5×Blue+1) | 高植被覆盖区 |
| **SAVI** | 土壤调节植被指数 | (NIR-Red)/(NIR+Red+0.5)×1.5 | 裸土区植被 |
| **MNDWI** | 修正水体指数 | (Green-SWIR)/(Green+SWIR) | 城市水体 |
| **AWEI** | 自动水体提取指数 | 4×(Green-SWIR)-(0.25×NIR+2.75×SWIR) | 自动水体 |
| **NBR** | 归一化燃烧指数 | (NIR-SWIR2)/(NIR+SWIR2) | 火烧迹地 |
| **BSI** | 裸土指数 | ((SWIR+Red)-(NIR+Blue))/((SWIR+Red)+(NIR+Blue)) | 裸土监测 |
| **UI** | 城市指数 | (SWIR2-NIR)/(SWIR2+NIR) | 城市建筑 |

## 参数一览 / Parameters

| 参数 | 说明 | 必填 |
|---|---|---|
| `input` | 输入 GeoTIFF 文件路径 | ✅ |
| `--index` | 指数名（空格分隔多个） | ✅（或 `--batch`） |
| `--batch` | 批量计算所有指数 | ❌ |
| `--formula` | 自定义公式（如 `(B4-B3)/(B4+B3)`） | ❌ |
| `--bands` | 波段顺序（如 `red nir green blue swir1 swir2`） | ❌ |
| `--output` | 输出文件/目录路径 | ❌ |

## License

MIT-0（详见 [LICENSE](./LICENSE)）。
零外部依赖，仅使用 Python 标准库（struct, os, sys）。
