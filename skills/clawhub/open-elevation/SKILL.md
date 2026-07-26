---
description: 'Batch query elevation data from the Open-Elevation public API. Supports
  single-point

  and multi-point queries by latitude/longitude coordinates. Outputs CSV or JSON.

  No API key required.

  '
name: open-elevation
---

# Open-Elevation

Query elevation (in meters) for any lat/lon coordinate on Earth using the free,
public [Open-Elevation](https://open-elevation.com/) API. No API key required.

## Features

- Single-point elevation lookup
- Batch queries from CSV files (up to 100 points per API call)
- Automatic chunking for large datasets
- CSV and JSON output
- Input validation for coordinates

## Usage

```bash
# Single point
python scripts\open-elevation.py lookup --lat 39.9042 --lon 116.4074

# JSON output
python scripts\open-elevation.py lookup --lat 39.9042 --lon 116.4074 --json

# Batch from CSV
python scripts\open-elevation.py batch --input coords.csv --output results.csv

# Batch to JSON
python scripts\open-elevation.py batch --input coords.csv --output results.json --json
```

## Installation

```bash
pip install requests>=2.28.0 tqdm
# Or: pip install -r scripts/requirements.txt
```

## Parameters

### `lookup`
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--lat` | Yes | — | Latitude (-90 to 90) |
| `--lon` | Yes | — | Longitude (-180 to 180) |
| `--json` | No | false | Output as JSON |

### `batch`
| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--input` | Yes | — | Input CSV path (must contain `lat`/`lon` or `latitude`/`longitude` columns) |
| `--output` | Yes | — | Output file path |
| `--json` | No | false | Output as JSON instead of CSV |
| `--chunk` | No | 100 | Points per API request (max 100) |

## Data Source

- **API**: [Open-Elevation](https://open-elevation.com/)
- **Endpoint**: `https://api.open-elevation.com/api/v1/lookup`
- **Coverage**: Global
- **License**: Public domain
- **Cost**: Free, no key required
- **Underlying data**: SRTM (Shuttle Radar Topography Mission), AW3D30 (ALOS World 3D - 30m), and other sources
- **CRS**: WGS84 (EPSG:4326)
- **Spatial resolution**: ~30m (SRTM 1-arc second), varies by region
- **Rate limit**: Max 100 points per API request; be respectful of the public service
- **Timeout**: Default 30s per request; configurable via `--timeout` flag

### Output Schema

**CSV columns**: `latitude`, `longitude`, `elevation`

**JSON format**:
```json
{
  "results": [
    {"latitude": 39.9042, "longitude": 116.4074, "elevation": 43.5}
  ]
}
```

### Ocean / Bathymetry Handling

- Ocean areas return elevation of `0` (sea level) or negative values (bathymetry) depending on data availability
- SRTM does not cover open ocean; ocean points may return `0`

### Citation

If you use SRTM data in publications, please cite:

```bibtex
@misc{srtm2000,
  title = {Shuttle Radar Topography Mission (SRTM) Global Data},
  author = {{NASA Jet Propulsion Laboratory}},
  year = {2000},
  howpublished = {\url{https://www2.jpl.nasa.gov/srtm/}},
  note = {Accessed: YYYY-MM-DD}
}
```

## Visualization

- Plot elevation profiles with `matplotlib`: `plt.plot(distance, elevation)`
- Create DEM heatmaps with `imshow()` using terrain colormaps (`cmap='terrain'`)
- Overlay on maps with `contextily` or `folium`

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue | Check internet, retry |
| `HTTP 429` | Rate limit | Wait 60s, retry |
| `ValueError` | Invalid input | Check parameter format |
| Empty output | No data | Try different parameters |
| `ModuleNotFoundError` | Missing dep | Run pip install |
| Timeout | Slow network | Increase `--timeout` value |
| All zeros in ocean | No SRTM coverage | Expected behavior for ocean points |

---

## Advanced Usage

### Large Batch Query with Retry
```python
import csv, time, subprocess
with open('points.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for attempt in range(3):
            result = subprocess.run(
                ['python', 'scripts/open_elevation.py', 'lookup',
                 '--lat', row['lat'], '--lon', row['lon']],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                break
            time.sleep(2 ** attempt)
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/elevation-update.yml
name: Elevation Data Update
on:
  workflow_dispatch:
jobs:
  query:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: |
          python scripts\open-elevation.py batch \
            --input points.csv --output elevations.json
```

### PostgreSQL/PostGIS Import
```bash
python scripts\open-elevation.py batch --input points.csv --output elevations.json

# Convert to CSV then import
python -c "import json, csv; d=json.load(open('elevations.json')); 
csv.writer(open('elev.csv','w',newline='')).writerows(
  [('lat','lon','elevation')] + [(p['lat'],p['lon'],p['elevation']) for p in d]
)"
psql -d gis_db -c "\COPY elevations(lat, lon, elevation) FROM 'elev.csv' CSV HEADER"
```

### Performance Tips
- Batch mode accepts up to 100 points per request; chunk large files
- Add `sleep 1` between batches to respect rate limits
- Ocean coordinates return 0m elevation — filter with `WHERE elevation != 0`

---

## 中文说明

使用免费的 [Open-Elevation](https://open-elevation.com/) 公开 API 查询任意经纬度的海拔高度（米）。无需 API 密钥。

### 功能

- 单点高程查询
- 从 CSV 文件批量查询（每次 API 调用最多 100 点）
- 大数据集自动分块
- 支持 CSV 和 JSON 输出
- 坐标输入验证

### 使用方法

```bash
# 单点查询
python scripts\open-elevation.py lookup --lat 39.9042 --lon 116.4074

# JSON 输出
python scripts\open-elevation.py lookup --lat 39.9042 --lon 116.4074 --json

# 批量查询
python scripts\open-elevation.py batch --input coords.csv --output results.csv

# 批量 JSON 输出
python scripts\open-elevation.py batch --input coords.csv --output results.json --json
```

### 数据来源

- **API**: [Open-Elevation](https://open-elevation.com/)
- **端点**: `https://api.open-elevation.com/api/v1/lookup`
- **覆盖范围**: 全球
- **许可证**: 公有领域
- **费用**: 免费，无需密钥
- **底层数据**: SRTM (航天飞机雷达地形测绘任务)、AW3D30 (ALOS World 3D - 30m) 等
- **坐标系**: WGS84 (EPSG:4326)
- **空间分辨率**: ~30m (SRTM 1角秒)，因地区而异
- **速率限制**: 每次 API 请求最多 100 点；请尊重公共服务
- **超时**: 默认 30 秒/请求；可通过 `--timeout` 参数配置

### 输出格式

**CSV 列**: `latitude`, `longitude`, `elevation`

**JSON 格式**:
```json
{
  "results": [
    {"latitude": 39.9042, "longitude": 116.4074, "elevation": 43.5}
  ]
}
```

### 海洋/水深处理

- 海洋区域返回海拔 `0`（海平面）或负值（水深），取决于数据可用性
- SRTM 不覆盖开阔海洋；海洋点可能返回 `0`

### 引用格式

如果发表使用 SRTM 数据，请引用:

```bibtex
@misc{srtm2000,
  title = {Shuttle Radar Topography Mission (SRTM) Global Data},
  author = {{NASA Jet Propulsion Laboratory}},
  year = {2000},
  howpublished = {\url{https://www2.jpl.nasa.gov/srtm/}},
  note = {Accessed: YYYY-MM-DD}
}
```

### 可视化

- 使用 `matplotlib` 绘制高程剖面: `plt.plot(distance, elevation)`
- 使用 `imshow()` + terrain 色标 (`cmap='terrain'`) 创建 DEM 热力图
- 使用 `contextily` 或 `folium` 叠加到地图上

### 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `ConnectionError` | 网络问题 | 检查网络，重试 |
| `HTTP 429` | 速率限制 | 等待 60 秒后重试 |
| `ValueError` | 无效输入 | 检查参数格式 |
| 空输出 | 无数据 | 尝试不同参数 |
| `ModuleNotFoundError` | 缺少依赖 | 运行 pip install |
| 超时 | 网络慢 | 增加 `--timeout` 值 |
| 海洋区域全为 0 | SRTM 无覆盖 | 海洋点的预期行为 |
