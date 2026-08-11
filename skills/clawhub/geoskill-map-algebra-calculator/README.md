# Map Algebra Calculator (geoskill-map-algebra-calculator)

> Evaluate band math expressions like NDVI on rasters with a safe expression parser

---

## 1. Overview

Performs map algebra on multi-band rasters using a **safe expression evaluator** based on Python `ast`, supporting band references b1..bN, the four basic arithmetic operations, powers, and common math functions, with built-in preset indices such as NDVI / NDWI / SAVI / EVI. Expressions pass a whitelist check that rejects attribute access, imports, and non-whitelisted calls; division by zero is automatically set to 0, so results contain no inf / nan.

## 2. Features

Performs map algebra on multi-band rasters using a **safe expression evaluator** based on Python `ast`, supporting band references b1..bN, the four basic arithmetic operations, powers, and common math functions, with built-in preset indices such as NDVI / NDWI / SAVI / EVI. Expressions pass a whitelist check that rejects attribute access, imports, and non-whitelisted calls; division by zero is automatically set to 0, so results contain no inf / nan.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-map-algebra-calculator.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

## 4. CLI Parameters

Run `python <skill>.py --help` for the full list. Common parameters:

| Parameter | Type | Description |
|---|---|---|
| `--bbox` | `float[4]` | WGS84 bounding box `min_lon min_lat max_lon max_lat` |
| `--input` | `path` | Local input file (GeoJSON/GeoTIFF/etc.) |
| `--output-dir` | `path` | Output directory (default `./output`) |
| `--synthetic` | `flag` | Use synthetic data instead of real input |
| `--quiet` | `flag` | Suppress non-essential stdout |

## 5. Input / Output

| File | Format | Description |
|---|---|---|
| `result.tif` | GeoTIFF | Result raster of the operation (primary/verifiable output) |
| `expression_meta.json` | JSON | Expression and result statistics |

Each run also produces `output-manifest.json` (run manifest).


## 6. Technical Principle

ast.parse(mode='eval') → whitelist recursive evaluation (numbers / bands / pi, e / whitelisted functions / + - * / % **) → division by zero set to 0 → float32 raster.

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# 地图代数计算器（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-map-algebra-calculator
description: 'Evaluate band math expressions like NDVI on rasters with a safe expression parser'
---

# 地图代数计算器 | Map Algebra Calculator

对多波段栅格做地图代数运算，用基于 Python ast 的**安全表达式求值器**支持波段引用 b1..bN、四则运算、幂与常用数学函数，内置 NDVI/NDWI/SAVI/EVI 等预设指数。

表达式经白名单校验，拒绝属性访问、导入与非白名单调用；除零自动置 0，结果无 inf/nan。

## 核心算法

ast.parse(mode='eval') → 白名单递归求值（数字/波段/pi,e/白名单函数/+-*/% **) → 除零置 0 → float32 栅格。

## 依赖

```bash
pip install numpy rasterio scipy matplotlib geopandas shapely pillow
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-map-algebra-calculator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（自定义表达式）

```bash
python geoskill-map-algebra-calculator.py --input scene.tif --expr "(b4-b3)/(b4+b3)"
```

### 示例 3（NDWI 预设）

```bash
python geoskill-map-algebra-calculator.py --input scene.tif --preset ndwi --green 2 --nir 4
```

### 示例 4（比值 + 缩放）

```bash
python geoskill-map-algebra-calculator.py --input scene.tif --expr "b2/b1 * 100"
```

### 示例 5（合成 NDVI）

```bash
python geoskill-map-algebra-calculator.py --bbox 116 39 117 40 --synthetic --preset ndvi
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `result.tif` | GeoTIFF | 运算结果栅格（主产物/可验证产物） |
| `expression_meta.json` | JSON | 表达式与结果统计 |

每次运行还会产出 `output-manifest.json`（运行清单）。

## 数据源 / Source

本地 GeoTIFF / 矢量文件；`--synthetic` 模式生成物理一致的模拟数据，完全离线。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
