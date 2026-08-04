---
name: forest-carbon-estimate
description: 'Estimate forest carbon stock from remote sensing data using BEF, allometric equations, or IPCC Tier 1/2 methods. Includes Monte Carlo uncertainty analysis. Supports raster (GeoTIFF) and tabular (CSV) inputs.'
---

# forest-carbon-estimate

Estimate forest carbon stock from remote sensing data using multiple methods with uncertainty analysis.

## Features

- **BEF Method**: Biomass Expansion Factor from AGB
- **Allometric Equations**: AGB = a × H^b from forest height
- **IPCC Tier 1/2**: Default factors by forest type
- **Monte Carlo Uncertainty**: Propagate input uncertainties
- **Raster Processing**: Direct GeoTIFF input/output
- **Tabular Processing**: CSV with plot-level data
- **Multiple Forest Types**: Tropical, temperate, boreal, mangrove

## Usage

```bash
# Single-point estimate (allometric)
python scripts\forest-carbon-estimate.py estimate --method allometric --height 15 --forest-type tropical

# Single-point estimate (BEF)
python scripts\forest-carbon-estimate.py estimate --method bef --agb 200 --forest-type temperate

# IPCC Tier 1 default
python scripts\forest-carbon-estimate.py estimate --method ipcc --forest-type boreal --area-ha 100

# Raster processing
python scripts\forest-carbon-estimate.py estimate --input height.tif --method allometric --output carbon.tif

# Uncertainty analysis
python scripts\forest-carbon-estimate.py uncertainty --method allometric --height 15 --iterations 5000

# Report from CSV
python scripts\forest-carbon-estimate.py report --input carbon_stock.csv
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--input` | Input GeoTIFF or CSV | None (single-point) |
| `--method` | Estimation method | allometric |
| `--forest-type` | Forest type for default factors | default |
| `--height` | Forest height (m) for allometric | None |
| `--agb` | Above-ground biomass (t/ha) for BEF | None |
| `--area-ha` | Area in hectares (IPCC) | 1.0 |
| `--agb-band` | Band number for raster input | 1 |
| `--iterations` | Monte Carlo iterations | 1000 |
| `--output` | Output file path | Auto-generated |

## Calculation Chain

```
AGB (Above-ground biomass)
  ↓
BGB = AGB × root_shoot_ratio (default 0.26)
  ↓
Total biomass = AGB + BGB
  ↓
Carbon stock = Total biomass × carbon_fraction (default 0.47)
```

## Methods

| Method | Input | Description |
|--------|-------|-------------|
| BEF | AGB (t/ha) | Total biomass = AGB × BEF |
| Allometric | Height (m) | AGB = a × H^b |
| IPCC | Forest type | Default density from IPCC tables |

## Installation

```bash
pip install requests>=2.28.0 tqdm numpy scipy rasterio
# Or: pip install -r scripts/requirements.txt
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical computation and Monte Carlo |
| `rasterio` | GeoTIFF I/O for raster mode |
| `scipy` | Statistical functions |
| `requests` | Data download (if applicable) |
| `tqdm` | Progress bars |

## Data Source

- IPCC Guidelines for National Greenhouse Gas Inventories (2006, 2019 Refinement)
- IPCC EFDB (Emission Factor Database)

## BEF Values per Forest Type

| Forest Type | BEF Range |
|-------------|-----------|
| Tropical | 1.5 – 3.0 |
| Temperate | 1.2 – 1.8 |
| Boreal | 1.0 – 1.5 |
| Mangrove | 1.2 – 1.8 |

Default BEF = 1.32 (temperate mixed forest). Adjust with `--bef` parameter.

## Allometric Coefficients

For AGB = a × H^b (H = forest height in m):

| Forest Type | a | b |
|-------------|------|------|
| Tropical | 0.0673 | 0.976 |
| Temperate | 0.0592 | 1.030 |
| Boreal | 0.0450 | 1.050 |

These are DBH-based defaults. For height-based allometry, use `--coeff-a` and `--coeff-b` to override.

## IPCC Default Wood Density

| Forest Type | Wood Density (g/cm³) |
|-------------|---------------------|
| Tropical | 0.57 – 0.69 |
| Temperate | 0.41 – 0.56 |
| Boreal | 0.38 – 0.51 |

Default: 0.55 g/cm³. Override with `--wood-density`.

## Method Selection Guidance

| Method | Best For | Input Required |
|--------|----------|----------------|
| BEF | Forest inventory data | AGB (t/ha) |
| Allometric | Remote sensing (LiDAR/InSAR height) | Forest height (m) |
| IPCC Tier 1 | Quick estimates, no field data | Forest type + area |

## Output Units

Carbon stock is reported in **Mg C/ha** (megagrams of carbon per hectare), equivalent to **t C/ha**.

For total stock: multiply by area (ha) → total Mg C.

## Nodata Handling

Nodata pixels in input rasters are skipped. Output GeoTIFF uses the same nodata value as input. No interpolation is performed on nodata areas.

## Custom Parameters

```bash
# Custom carbon fraction and root-shoot ratio
python scripts\forest-carbon-estimate.py estimate --method bef --agb 200 --forest-type temperate --carbon-fraction 0.45 --root-shoot-ratio 0.28
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--carbon-fraction` | 0.47 | Carbon fraction of dry biomass |
| `--root-shoot-ratio` | 0.26 | Root-to-shoot ratio |
| `--bef` | 1.32 | Biomass expansion factor |

## Uncertainty Output Structure

```json
{
  "mean": 125.3,
  "std": 18.7,
  "CI95_lower": 88.6,
  "CI95_upper": 162.0
}
```

| Field | Description |
|-------|-------------|
| `mean` | Mean carbon stock estimate (Mg C/ha) |
| `std` | Standard deviation from Monte Carlo |
| `CI95_lower` | 95% confidence interval lower bound |
| `CI95_upper` | 95% confidence interval upper bound |

## Data Acquisition Guidance

Obtain forest height/AGB rasters from:
- **Global Forest Watch** (https://www.globalforestwatch.org/) — AGB maps
- **NASA GEDI** (https://gedi.umd.edu/) — Forest height from spaceborne LiDAR
- **ESA Biomass Mission** — P-band SAR forest height
- **National forest inventory** — Plot-level AGB data

## Validation / Quality Assessment

- Compare with field-measured carbon stock plots
- Cross-validate with IPCC default values for the same forest type
- Check that uncertainty range (CI95) is reasonable (< 50% of mean)
- Report method, forest type, and input data source in publications

## Citation

```bibtex
@book{ipcc2006guidelines,
  title={2006 IPCC Guidelines for National Greenhouse Gas Inventories},
  author={{IPCC}},
  year={2006},
  publisher={Institute for Global Environmental Strategies},
  url={https://www.ipcc-nggip.iges.or.jp/public/2006gl/}
}
@book{ipcc2019refinement,
  title={2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories},
  author={{IPCC}},
  year={2019},
  publisher={IPCC},
  url={https://www.ipcc-nggip.iges.or.jp/public/2019rf/}
}
```

## Visualization Guidance

```python
import rasterio
import matplotlib.pyplot as plt
import numpy as np

with rasterio.open("carbon.tif") as src:
    carbon = src.read(1)
    nodata = src.nodata

carbon_plot = np.where(carbon == nodata, np.nan, carbon)

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(carbon_plot, cmap="Greens", vmin=0, vmax=200)
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("Carbon Stock (Mg C/ha)")
ax.set_title("Forest Carbon Stock")
ax.axis("off")
plt.tight_layout()
plt.savefig("carbon_map.png", dpi=200)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue | Check internet, retry |
| `HTTP 429` | Rate limit | Wait 60s, retry |
| `ValueError` | Invalid input | Check parameter format |
| Empty output | No data | Try different parameters |
| `ModuleNotFoundError` | Missing dep | Run pip install |

---

## Advanced Usage

### Batch Raster Processing
```bash
for year in 2020 2021 2022 2023; do
  python scripts\forest-carbon-estimate.py estimate     --input agb_${year}.tif --method allometric     --output carbon_${year}.tif
done
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/carbon-update.yml
name: Forest Carbon Update
on:
  schedule:
    - cron: '0 0 1 1 *'  # Yearly
jobs:
  estimate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install numpy rasterio
      - run: |
          python scripts\forest-carbon-estimate.py estimate \
            --input data/agb_latest.tif \
            --method allometric \
            --output data/carbon_latest.tif
```

### PostGIS Raster Import
```bash
raster2pgsql -s 4326 -I -C carbon_latest.tif public.forest_carbon | psql -d gis_db
```

### Performance Tips
- `--method bef` is fastest for regional estimates; `--method allometric` for species-specific
- Use `--carbon-fraction 0.47` to match local species (default 0.47 = IPCC default)
- For large rasters, process in tiles using `--window` parameter

---

## 中文说明

基于遥感数据估算森林碳储量，支持 BEF、异速生长方程、IPCC Tier 1/2 三种方法，含蒙特卡洛不确定性分析。

## 安装

```bash
pip install requests>=2.28.0 tqdm numpy scipy rasterio
# 或: pip install -r scripts/requirements.txt
```

## 依赖

| 包 | 用途 |
|-----|------|
| `numpy` | 数值计算和蒙特卡洛 |
| `rasterio` | 栅格模式 GeoTIFF 读写 |
| `scipy` | 统计函数 |
| `requests` | 数据下载（如适用） |
| `tqdm` | 进度条 |

## 各森林类型 BEF 值

| 森林类型 | BEF 范围 |
|----------|----------|
| 热带 | 1.5 – 3.0 |
| 温带 | 1.2 – 1.8 |
| 寒带 | 1.0 – 1.5 |
| 红树林 | 1.2 – 1.8 |

默认 BEF = 1.32（温带混交林）。使用 `--bef` 参数调整。

## 异速生长系数

AGB = a × H^b（H = 树高，单位 m）：

| 森林类型 | a | b |
|----------|------|------|
| 热带 | 0.0673 | 0.976 |
| 温带 | 0.0592 | 1.030 |
| 寒带 | 0.0450 | 1.050 |

这些是基于 DBH 的默认值。树高异速生长使用 `--coeff-a` 和 `--coeff-b` 覆盖。

## IPCC 默认木材密度

| 森林类型 | 木材密度 (g/cm³) |
|----------|-----------------|
| 热带 | 0.57 – 0.69 |
| 温带 | 0.41 – 0.56 |
| 寒带 | 0.38 – 0.51 |
