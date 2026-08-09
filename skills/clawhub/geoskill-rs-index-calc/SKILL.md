---
name: rs-index-calc
description: 'Calculate spectral indices from GeoTIFF imagery using pure Python. description: 'Calculate spectral indices from GeoTIFF imagery using pure Python.  No external dependencies required. Supports 10 indices including  NDVI, NDBI, NDWI, EVI, SAVI, MNDWI, AWEI, NBR, BSI, UI.  '
---

# Remote Sensing Index Calculator

Calculate spectral indices from GeoTIFF imagery using pure Python. No external dependencies required.

## Features

- **10 Supported Indices**: NDVI, NDBI, NDWI, EVI, SAVI, MNDWI, AWEI, NBR, BSI, UI
- **Pure Python**: No rasterio, GDAL, numpy, or scipy required
- **Auto Band Detection**: Automatically detects band mapping from GeoTIFF metadata
- **Custom Formulas**: Support for arbitrary band math expressions
- **Batch Mode**: Calculate all indices at once
- **Statistics**: Automatic min/max/mean/std computation

## Installation

```bash
pip install -r requirements.txt
# No external dependencies - uses only Python standard library
```

## Usage

### Single Index
```bash
python rs-index-calc.py input.tif NDVI
python rs-index-calc.py input.tif NDVI --output ndvi_result.tif
```

### All Indices (Batch Mode)
```bash
python rs-index-calc.py input.tif --batch
```

### Custom Formula
```bash
python rs-index-calc.py input.tif custom --formula "(B4-B3)/(B4+B3)"
```

### Manual Band Order
```bash
python rs-index-calc.py input.tif NDVI --bands red nir green blue swir1 swir2
```

## Supported Indices

| Index | Formula | Bands |
|-------|---------|-------|
| NDVI | (NIR - Red) / (NIR + Red) | NIR, Red |
| NDBI | (SWIR - NIR) / (SWIR + NIR) | SWIR, NIR |
| NDWI | (Green - NIR) / (Green + NIR) | Green, NIR |
| EVI | 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1) | NIR, Red, Blue |
| SAVI | (NIR - Red) / (NIR + Red + 0.5) * 1.5 | NIR, Red |
| MNDWI | (Green - SWIR) / (Green + SWIR) | Green, SWIR |
| AWEI | 4*(Green-SWIR) - (0.25*NIR + 2.75*SWIR) | Green, SWIR, NIR |
| NBR | (NIR - SWIR2) / (NIR + SWIR2) | NIR, SWIR2 |
| BSI | ((SWIR+Red)-(NIR+Blue)) / ((SWIR+Red)+(NIR+Blue)) | SWIR, Red, NIR, Blue |
| UI | (SWIR2 - NIR) / (SWIR2 + NIR) | SWIR2, NIR |

## Output

- Single-band GeoTIFF with calculated index values
- Statistics printed to stdout (min, max, mean, std, pixel count)

## Testing

```bash
pytest
```

## License

MIT-0 (No Attribution)

---

## 中文说明

从 GeoTIFF 影像计算光谱指数，纯 Python 实现，无需任何外部依赖。

### 支持的指数（10 种）

| 指数 | 公式 | 波段 |
|---|---|---|
| NDVI | (NIR - Red) / (NIR + Red) | NIR, Red |
| NDBI | (SWIR - NIR) / (SWIR + NIR) | SWIR, NIR |
| NDWI | (Green - NIR) / (Green + NIR) | Green, NIR |
| EVI | 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1) | NIR, Red, Blue |
| SAVI | (NIR - Red) / (NIR + Red + 0.5) * 1.5 | NIR, Red |
| MNDWI | (Green - SWIR) / (Green + SWIR) | Green, SWIR |
| AWEI | 4*(Green-SWIR) - (0.25*NIR + 2.75*SWIR) | Green, SWIR, NIR |
| NBR | (NIR - SWIR2) / (NIR + SWIR2) | NIR, SWIR2 |
| BSI | ((SWIR+Red)-(NIR+Blue)) / ((SWIR+Red)+(NIR+Blue)) | SWIR, Red, NIR, Blue |
| UI | (SWIR2 - NIR) / (SWIR2 + NIR) | SWIR2, NIR |

### 使用方法

```bash
# 计算单个指数
python rs-index-calc.py input.tif NDVI
python rs-index-calc.py input.tif NDVI --output ndvi_result.tif

# 批量计算所有指数
python rs-index-calc.py input.tif --batch

# 自定义公式
python rs-index-calc.py input.tif custom --formula "(B4-B3)/(B4+B3)"

# 手动指定波段顺序
python rs-index-calc.py input.tif NDVI --bands red nir green blue swir1 swir2
```

### 输出

- 单波段 GeoTIFF，值为指数计算结果
- 自动输出统计信息（最小值、最大值、均值、标准差、像元数）
