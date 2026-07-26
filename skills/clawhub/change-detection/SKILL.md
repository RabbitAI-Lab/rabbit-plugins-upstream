---
description: 'Multi-temporal change detection for satellite imagery using NDVI difference,

  image differencing, and Change Vector Analysis (CVA). Detects vegetation,

  urban, and water changes.

  '
name: change-detection
---

# Change Detection

Detect land cover changes between two satellite images using multiple methods: NDVI difference, image differencing, and Change Vector Analysis (CVA).

## Features

- **NDVI Difference**: ΔNDVI = NDVI_t2 − NDVI_t1 — vegetation change
- **Image Differencing**: Per-band difference — general change
- **Change Vector Analysis (CVA)**: Multi-band magnitude + direction
- **Binary change mask** with configurable threshold
- **Statistics report** with change percentages
- Supports Landsat 8/9 and Sentinel-2

## Band Configuration

| Sensor | Green | NIR | Red | SWIR |
|--------|-------|-----|-----|------|
| Landsat 8/9 | B3 | B5 | B4 | B6 |
| Sentinel-2 | B3 | B8 | B4 | B11 |

## Usage

### Detect vegetation change (NDVI difference)
```bash
python scripts\change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method ndvi-diff \
  --output change_magnitude.tif \
  --mask change_mask.tif
```

### Change Vector Analysis
```bash
python scripts\change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method cva \
  --output cva_magnitude.tif \
  --mask cva_mask.tif --threshold 0.15
```

### Generate report
```bash
python scripts\change-detection.py report \
  --mask change_mask.tif --json report.json
```

## Installation

```bash
pip install rasterio>=1.3.0 numpy>=1.21.0 tqdm>=4.64.0
# Or: pip install -r scripts/requirements.txt
```

## Parameters

- `--image-t1`: Path to time-1 image (earlier)
- `--image-t2`: Path to time-2 image (later)
- `--sensor`: Sensor type (`landsat8`, `landsat9`, `sentinel2`)
- `--method`: Detection method (`ndvi-diff`, `image-diff`, `cva`)
- `--output`: Output change magnitude GeoTIFF
- `--mask`: Output binary change mask
- `--threshold`: Change threshold (default: auto via Otsu)
- `--bands`: Comma-separated band indices for CVA (default: all)
- `--json`: Output statistics as JSON

## Output

- **Change magnitude**: Float GeoTIFF showing change intensity
- **Binary mask**: 1=change, 0=no change
- **Statistics**: Change pixel count, percentage, method used

## Dependencies

```
rasterio>=1.3.0
numpy>=1.21.0
tqdm>=4.64.0
```

## Method Selection Guidance

| Method | Best For | Input Requirements |
|--------|----------|-------------------|
| `ndvi-diff` | Vegetation change (growth, deforestation, crop shift) | Red + NIR bands |
| `image-diff` | General land cover change (any type) | Same bands in both images |
| `cva` | Multi-band change, direction matters | 2+ matching bands |

**Recommendation**: Start with `ndvi-diff` for vegetation studies; use `cva` when change direction (e.g., vegetation → urban) is important.

## Co-registration Guidance

Misaligned images cause false changes. Before running detection:

- Ensure both images share the **same CRS and resolution**
- Use image registration tools (e.g., `gdalwarp -tps`, ENVI Auto-Registration, or QGIS Coregistration plugins)
- Sub-pixel alignment (<0.5 pixel RMSE) recommended for pixel-based methods
- Verify alignment by overlaying both images and checking stable features (roads, buildings)

## CVA Direction Output

CVA produces two outputs:

- **Magnitude**: Change intensity (float GeoTIFF) — higher = more change
- **Direction (angle)**: Indicates change type based on band contribution

| Angle Range | Typical Interpretation |
|-------------|----------------------|
| 0°–90° | Increase in both bands (e.g., vegetation growth) |
| 90°–180° | Band 1 decreases, Band 2 increases |
| 180°–270° | Decrease in both bands (e.g., vegetation loss) |
| 270°–360° | Band 1 increases, Band 2 decreases |

Use `--direction-output cva_direction.tif` to save the angle raster.

## Cross-Sensor Guidance

Comparing images from different sensors (e.g., Landsat 8 vs Sentinel-2):

- **Normalize radiometry**: Apply relative radiometric normalization (e.g., histogram matching, IR-MAD)
- **Match resolutions**: Resample to coarser resolution
- **Same season**: Use images from similar phenological stage
- **Caution**: Cross-sensor comparison introduces additional uncertainty

## Cloud Masking Guidance

Clouds cause false change detections:

- Pre-filter images with <10% cloud cover
- Use QA_PIXEL band to mask clouds in both images
- Consider temporal compositing (e.g., monthly median) to reduce cloud impact

## Batch Processing

Process multiple image pairs with a CSV list:

```bash
python scripts\change-detection.py batch \
  --pair-list pairs.csv --sensor landsat8 --method ndvi-diff \
  --output-dir ./results/
```

`pairs.csv` format: `image_t1,image_t2,output_name`

## Vector Output

Convert change masks to vector polygons for GIS analysis:

```bash
python scripts\change-detection.py vectorize \
  --mask change_mask.tif --output change_polygons.geojson --min-area 500
```

Outputs GeoJSON or Shapefile with change area attributes.

## Visualization

- **Change magnitude**: Apply diverging colormap (blue=no change, red=high change)
- **Binary mask**: Overlay change areas in red on RGB composite
- **CVA direction**: Use cyclic colormap (HSV) for angle visualization
- **Side-by-side**: Show t1 image, t2 image, and change map together

## Citation

```bibtex
@software{change_detection,
  author  = {ruiduobao},
  title   = {Change Detection Tool},
  url     = {https://github.com/ruiduobao/change-detection},
  version = {0.1.0},
  year    = {2024},
}
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue | Check internet, retry |
| `HTTP 429` | Rate limit | Wait 60s, retry |
| `ValueError` | Invalid input | Check parameter format |
| Empty output | No change detected | Lower threshold or check input |
| `ModuleNotFoundError` | Missing dep | Run pip install |
| Misregistration artifacts | Images not aligned | Co-register before detection |
| Striped output | Cloud shadow | Apply cloud masking |

## Data Source

Local raster processing — two co-registered GeoTIFF images required.

---

## Advanced Usage

### Batch Multi-Pair Detection
```bash
for year in 2020 2021 2022 2023; do
  python scripts\change-detection.py detect     --image-t1 ${year}0101.tif --image-t2 $((year+1))0101.tif     --sensor landsat8 --method ndvi-diff     --output change_${year}_$((year+1)).tif
done
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/change-detection.yml
name: Change Detection Pipeline
on:
  schedule:
    - cron: '0 6 1 */3 *'  # Every 3 months
jobs:
  detect:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install numpy rasterio
      - run: |
          python scripts\change-detection.py detect \
            --image-t1 data/latest_2023.tif \
            --image-t2 data/latest_2024.tif \
            --sensor landsat8 --method ndvi-diff \
            --output data/change_latest.tif
```

### Vectorize & Import to PostGIS
```bash
python scripts\change-detection.py vectorize   --input change_mask.tif --output change.geojson

ogr2ogr -f PostgreSQL PG:"dbname=gis_db" change.geojson -nln change_areas
```

### Performance Tips
- Use `--mask` with QA band to exclude clouds before detection
- CVA method requires more memory; use `--bands` to limit input bands
- `--threshold` accepts 'otsu' (auto) or manual float value

---

## 中文说明

对两期卫星影像进行变化检测，支持 NDVI 差值、影像差值和变化向量分析（CVA）三种方法。

## 功能特性

- **NDVI 差值**：ΔNDVI = NDVI_t2 − NDVI_t1 — 植被变化
- **影像差值**：逐波段差值 — 通用变化
- **变化向量分析（CVA）**：多波段变化强度 + 方向
- **二值变化掩膜**，可配置阈值
- **统计报告**，含变化百分比
- 支持 Landsat 8/9 和 Sentinel-2

## 波段配置

| 传感器 | Green | NIR | Red | SWIR |
|--------|-------|-----|-----|------|
| Landsat 8/9 | B3 | B5 | B4 | B6 |
| Sentinel-2 | B3 | B8 | B4 | B11 |

## 使用示例

### 植被变化检测（NDVI 差值）
```bash
python scripts\change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method ndvi-diff \
  --output change_magnitude.tif \
  --mask change_mask.tif
```

### 变化向量分析
```bash
python scripts\change-detection.py detect \
  --image-t1 2020.tif --image-t2 2023.tif \
  --sensor landsat8 --method cva \
  --output cva_magnitude.tif \
  --mask cva_mask.tif --threshold 0.15
```

### 生成报告
```bash
python scripts\change-detection.py report \
  --mask change_mask.tif --json report.json
```

## 安装

```bash
pip install rasterio>=1.3.0 numpy>=1.21.0 tqdm>=4.64.0
# 或: pip install -r scripts/requirements.txt
```

## 参数说明

- `--image-t1`: 时相 1 影像路径（早期）
- `--image-t2`: 时相 2 影像路径（晚期）
- `--sensor`: 传感器类型
- `--method`: 检测方法（`ndvi-diff`, `image-diff`, `cva`）
- `--output`: 输出变化强度 GeoTIFF
- `--mask`: 输出二值变化掩膜
- `--threshold`: 变化阈值（默认 Otsu 自动）
- `--bands`: CVA 使用的波段索引（逗号分隔，默认全部）
- `--json`: 以 JSON 输出统计信息

## 输出结果

- **变化强度**: 浮点 GeoTIFF，显示变化强度
- **二值掩膜**: 1=变化, 0=无变化
- **统计信息**: 变化像素数、占比、使用方法

## 依赖库

```
rasterio>=1.3.0
numpy>=1.21.0
tqdm>=4.64.0
```

## 方法选择指南

| 方法 | 适用场景 | 输入要求 |
|------|---------|---------|
| `ndvi-diff` | 植被变化（生长、砍伐、作物变化） | Red + NIR 波段 |
| `image-diff` | 通用土地覆盖变化 | 两幅影像波段一致 |
| `cva` | 多波段变化，方向重要 | 2+ 匹配波段 |

**建议**：植被研究先用 `ndvi-diff`；需要变化方向信息时用 `cva`。

## 配准指导

未对齐的影像会导致虚假变化。检测前请确保：

- 两幅影像使用 **相同的 CRS 和分辨率**
- 使用影像配准工具（如 `gdalwarp -tps`、ENVI 自动配准、QGIS 配准插件）
- 像元方法建议亚像元对齐（<0.5 像元 RMSE）
- 叠加两幅影像检查稳定地物（道路、建筑）验证对齐

## CVA 方向输出

CVA 产生两个输出：

- **强度**：变化强度（浮点 GeoTIFF）— 值越大变化越强
- **方向（角度）**：根据波段贡献指示变化类型

| 角度范围 | 典型解释 |
|---------|---------|
| 0°–90° | 两个波段均增加（如植被生长） |
| 90°–180° | 波段 1 减少，波段 2 增加 |
| 180°–270° | 两个波段均减少（如植被损失） |
| 270°–360° | 波段 1 增加，波段 2 减少 |

使用 `--direction-output cva_direction.tif` 保存角度栅格。

## 跨传感器指导

比较不同传感器影像（如 Landsat 8 vs Sentinel-2）：

- **辐射归一化**：应用相对辐射归一化（如直方图匹配、IR-MAD）
- **分辨率匹配**：重采样至较粗分辨率
- **同季节**：使用相似物候期的影像
- **注意**：跨传感器比较引入额外不确定性 |

## 云掩膜指导

云会导致虚假变化检测：

- 预过滤云量 <10% 的影像
- 使用 QA_PIXEL 波段掩膜两幅影像中的云
- 考虑时间合成（如月际中值）减少云影响

## 批量处理

使用 CSV 列表处理多对影像：

```bash
python scripts\change-detection.py batch \
  --pair-list pairs.csv --sensor landsat8 --method ndvi-diff \
  --output-dir ./results/
```

`pairs.csv` 格式：`image_t1,image_t2,output_name`

## 矢量输出

将变化掩膜转换为矢量多边形用于 GIS 分析：

```bash
python scripts\change-detection.py vectorize \
  --mask change_mask.tif --output change_polygons.geojson --min-area 500
```

输出 GeoJSON 或 Shapefile，含变化面积属性。

## 可视化

- **变化强度**：发散色阶（蓝=无变化，红=高变化）
- **二值掩膜**：在 RGB 合成图上叠加红色变化区域
- **CVA 方向**：使用循环色阶（HSV）可视化角度
- **对比**：同时展示时相 1、时相 2 和变化图

## 引用格式

```bibtex
@software{change_detection,
  author  = {ruiduobao},
  title   = {Change Detection Tool},
  url     = {https://github.com/ruiduobao/change-detection},
  version = {0.1.0},
  year    = {2024},
}
```

## 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `ConnectionError` | 网络问题 | 检查网络，重试 |
| `HTTP 429` | 速率限制 | 等待 60 秒后重试 |
| `ValueError` | 无效输入 | 检查参数格式 |
| 无输出 | 未检测到变化 | 降低阈值或检查输入 |
| `ModuleNotFoundError` | 缺少依赖 | 运行 pip install |
| 配准伪影 | 影像未对齐 | 先配准再检测 |
| 条带状输出 | 云影 | 应用云掩膜 |

## 数据来源

本地栅格处理 — 需要两幅配准好的 GeoTIFF 影像。
