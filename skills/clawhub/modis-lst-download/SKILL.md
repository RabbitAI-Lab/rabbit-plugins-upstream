---
name: modis-lst-download
description: 'Search and download MODIS Land Surface Temperature (LST) products from description: 'Search and download MODIS Land Surface Temperature (LST) products from NASA LAADS DAAC.  Supports MOD11A1 (daily 1km), MOD11A2 (8-day 1km), MYD11A1, and MYD11A2 from  Terra and Aqua satellites. Outputs GeoTIFF format.  '
---

# MODIS Land Surface Temperature Download

Search and download MODIS LST products from NASA LAADS DAAC with Earthdata authentication.

## Overview

MODIS Land Surface Temperature (LST) products provide per-pixel land surface temperature
with 1km spatial resolution. This skill supports both Terra (MOD) and Aqua (MYD) satellite
products at daily and 8-day composite intervals.

## Products

| Product | Satellite | Temporal | Resolution |
|---------|-----------|----------|------------|
| MOD11A1 | Terra | Daily | 1km |
| MOD11A2 | Terra | 8-day | 1km |
| MYD11A1 | Aqua | Daily | 1km |
| MYD11A2 | Aqua | 8-day | 1km |

## Features

- **Day and night LST**: separate daytime and nighttime temperature layers
- **Quality control**: includes QC bands for quality filtering
- **Search by date range and bbox**: find available granules
- **GeoTIFF output**: standard georeferenced raster format
- **Earthdata authentication**: secure access to NASA data
- **Fallback URL listing**: shows download URLs even without credentials

## Authentication

NASA Earthdata requires a free account. To configure:

1. Register at https://urs.earthdata.nasa.gov/
2. Set environment variables:
   ```bash
   export EARTHDATA_USERNAME="your_username"
   export EARTHDATA_PASSWORD="your_password"
   ```
3. Or use the configure command:
   ```bash
   python scripts\modis_lst_download.py configure --username your_username
   ```

## Usage

```bash
# Search for available LST data
python scripts\modis_lst_download.py search \
  --product MOD11A1 \
  --start 2023-06-01 --end 2023-06-30 \
  --bbox 116.0 39.5 116.8 40.2

# Download daily LST (requires Earthdata auth)
python scripts\modis_lst_download.py download \
  --product MOD11A1 \
  --start 2023-07-01 --end 2023-07-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --output ./lst_data/ --layers LST_Day_1km,QC_Day

# Download 8-day composite
python scripts\modis_lst_download.py download \
  --product MOD11A2 \
  --start 2023-07-01 --end 2023-07-08 \
  --bbox 73 18 135 54 \
  --output ./china_lst/

# List download URLs without downloading
python scripts\modis_lst_download.py download \
  --product MYD11A1 \
  --start 2023-08-01 --end 2023-08-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --list-only
```

## Parameters

- `--product`: MOD11A1, MOD11A2, MYD11A1, or MYD11A2
- `--start/--end`: Date range (YYYY-MM-DD)
- `--bbox`: Bounding box as `west south east north`
- `--output`: Output directory
- `--layers`: Comma-separated layer names (LST_Day_1km, LST_Night_1km, QC_Day, QC_Night)
- `--list-only`: Only list download URLs, do not download
- `--username`: Earthdata username (or set EARTHDATA_USERNAME env var)

## Installation

```bash
# Install dependencies
pip install requests>=2.28.0 tqdm

# Or install from requirements.txt
pip install -r scripts/requirements.txt
```

## Data Source

- **API**: NASA LAADS DAAC (https://ladsweb.modaps.eosdis.nasa.gov/)
- **Search API**: CMR (Common Metadata Repository) via CMR-STAC
- **License**: Public Domain (NASA open data)
- **Rate Limit**: No strict limit; recommended max 10 requests/minute
- **CRS**: Sinusoidal (MODIS native projection)
- **Temporal coverage**: Terra from 2000-02-24; Aqua from 2002-07-04
- **Data latency**: ~2 weeks for standard products

### Product Citations

- **MOD11A1**: Wan, Z., S. Hook, and G. Hulley, 2015. MOD11A1 MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V006. NASA EOSDIS Land Processes DAAC.
- **MOD11A2**: Wan, Z., S. Hook, and G. Hulley, 2015. MOD11A2 MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006. NASA EOSDIS Land Processes DAAC.
- **MYD11A1**: Wan, Z., S. Hook, and G. Hulley, 2015. MYD11A1 MODIS/Aqua Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V006. NASA EOSDIS Land Processes DAAC.
- **MYD11A2**: Wan, Z., S. Hook, and G. Hulley, 2015. MYD11A2 MODIS/Aqua Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006. NASA EOSDIS Land Processes DAAC.

### Citation Format

```bibtex
@misc{wan2015mod11a2,
  title={MOD11A2 MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006},
  author={Wan, Z. and Hook, S. and Hulley, G.},
  journal={NASA EOSDIS Land Processes DAAC},
  year={2015},
  doi={10.5067/MODIS/MOD11A2.006}
}
```

### LST Scale Factor

- **Raw values**: Integer DN (Digital Number)
- **Conversion**: Multiply by `0.02` to get temperature in **Kelvin**
- **To Celsius**: `T(°C) = DN × 0.02 - 273.15`
- Example: DN `15000` → 300.00 K → 26.85°C

### QC Band Interpretation

| Bits | Field | Values |
|------|-------|--------|
| 0-1 | Quality flag | 0=good quality, 1=other quality, 2=cloud contaminated, 3=not produced |
| 2-3 | Emissivity error flag | 0=≤0.01, 1=≤0.02, 2=≤0.04, 3=>0.04 |
| 4-5 | LST error flag | 0=≤1K, 1=≤2K, 2=≤3K, 3=>3K |

**Cloud filtering**: Keep only pixels where bits 0-1 = 0 (good quality).

### 8-Day Compositing Algorithm

MOD11A2 composites daily LST values over 8 days using:
- **Cloud-free preference**: Pixels with no cloud contamination are prioritized.
- **Maximum temperature**: For overlapping observations, the highest quality LST value is retained.
- **QC-driven**: Only pixels passing QC checks are included in the composite.

### Visualization

- **Temperature maps**: Load GeoTIFF in QGIS with single-band pseudocolor, apply color ramp (blue→red).
- **Time series**: Stack multiple dates and plot with matplotlib.
- **QC overlay**: Use QC band to mask unreliable pixels before visualization.

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue or API down | Check internet connection, retry in 1 minute |
| `HTTP 429` | Rate limit exceeded | Wait 60 seconds before retrying |
| `HTTP 404` | Invalid parameters or date range | Check parameter names and date format |
| `ValueError: bbox` | Invalid bounding box | Ensure format is `west,south,east,north` |
| Empty output | No data for query region/time | Try different date range or check coordinates |
| `ModuleNotFoundError` | Missing dependency | Run `pip install requests tqdm` |
| `401 Unauthorized` | Earthdata auth failed | Check EARTHDATA_USERNAME/PASSWORD or run `configure` |

---

## Advanced Usage

### Batch Time Series Download
```bash
# Download every month for a year
for month in $(seq -w 1 12); do
  python scripts\modis_lst_download.py download     --product MOD11A1 --bbox 116 39.5 117 40.2     --start 2023-${month}-01 --end 2023-${month}-28     --output lst_2023_${month}.tif
  sleep 2
done
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/update-modis-lst.yml
name: Update MODIS LST
on:
  schedule:
    - cron: '0 12 * * *'  # Daily
jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - env:
          EARTHDATA_USERNAME: ${{ secrets.EARTHDATA_USER }}
          EARTHDATA_PASSWORD: ${{ secrets.EARTHDATA_PASS }}
        run: |
          python scripts\modis_lst_download.py download \
            --product MOD11A1 --bbox 116 39.5 117 40.2 \
            --start $(date -d '3 days ago' +%Y-%m-%d) \
            --end $(date +%Y-%m-%d) \
            --output data/lst_latest.tif
```

### LST Conversion & QC
```python
import rasterio
import numpy as np
with rasterio.open('lst.tif') as src:
    raw = src.read(1)
    # Convert DN to Celsius: scale factor 0.02, offset 273.15
    lst_celsius = raw * 0.02 - 273.15
    # QC: use QC band bits 0-1, keep only value 0 (good quality)
```

### PostgreSQL/PostGIS Raster Import
```bash
raster2pgsql -s 4326 -I -C lst.tif public.lst_raster | psql -d gis_db
```

### Performance Tips
- Use `--list-only` first to preview URLs, then download in parallel
- Add `sleep 2` between requests to avoid NASA rate limits
- For time series analysis, prefer MOD11A2 (8-day composite) over MOD11A1 to reduce cloud contamination

---

## 中文说明

从 NASA LAADS DAAC 搜索和下载 MODIS 地表温度（LST）产品。支持 Terra 和 Aqua 卫星的逐日和 8 天合成产品。

### 产品列表

| 产品 | 卫星 | 时间分辨率 | 空间分辨率 |
|------|------|-----------|-----------|
| MOD11A1 | Terra | 逐日 | 1km |
| MOD11A2 | Terra | 8天合成 | 1km |
| MYD11A1 | Aqua | 逐日 | 1km |
| MYD11A2 | Aqua | 8天合成 | 1km |

### 核心功能

- **昼夜地表温度**：分别获取白天和夜间温度图层
- **质量控制**：包含 QC 波段用于质量过滤
- **按日期范围和区域搜索**：查找可用数据
- **GeoTIFF 输出**：标准地理参考栅格格式
- **Earthdata 认证**：安全访问 NASA 数据
- **URL 列表回退**：无认证时仍可列出下载链接

### 认证说明

NASA Earthdata 需要免费账号。配置方法：

1. 在 https://urs.earthdata.nasa.gov/ 注册
2. 设置环境变量：
   ```bash
   set EARTHDATA_USERNAME=your_username
   set EARTHDATA_PASSWORD=your_password
   ```
3. 或使用 configure 命令：
   ```bash
   python scripts\modis_lst_download.py configure --username your_username
   ```

### 使用示例

```bash
# 搜索可用 LST 数据
python scripts\modis_lst_download.py search \
  --product MOD11A1 \
  --start 2023-06-01 --end 2023-06-30 \
  --bbox 116.0 39.5 116.8 40.2

# 下载逐日 LST（需要 Earthdata 认证）
python scripts\modis_lst_download.py download \
  --product MOD11A1 \
  --start 2023-07-01 --end 2023-07-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --output ./lst_data/ --layers LST_Day_1km,QC_Day

# 下载 8 天合成产品
python scripts\modis_lst_download.py download \
  --product MOD11A2 \
  --start 2023-07-01 --end 2023-07-08 \
  --bbox 73 18 135 54 \
  --output ./china_lst/

# 仅列出下载 URL 不下载
python scripts\modis_lst_download.py download \
  --product MYD11A1 \
  --start 2023-08-01 --end 2023-08-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --list-only
```

### 数据来源

- **API**: NASA LAADS DAAC (https://ladsweb.modaps.eosdis.nasa.gov/)
- **搜索 API**: CMR (Common Metadata Repository) via CMR-STAC
- **许可证**: 公共领域（NASA 开放数据）
- **引用**: Wan, Z., S. Hook, and G. Hulley, 2015. MOD11A2 MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006. NASA EOSDIS Land Processes DAAC.
