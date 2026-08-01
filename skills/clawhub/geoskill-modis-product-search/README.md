# modis-product-skill

> Comprehensive local query tool for NASA MODIS satellite products.
> Covers 46 products across 13 categories with bilingual (Chinese/English) descriptions,
> algorithm principles, band information, Google Earth Engine integration, and download info.
>
> 全面的 NASA MODIS 卫星产品本地查询工具。涵盖 46 个产品、13 个类别，
> 提供双语（中英文）介绍、算法原理、波段信息、Google Earth Engine 集成和下载信息。

## Features

- **46 products** across 13 categories (vegetation, temperature, fire, snow, etc.)
- **Bilingual search** — query in Chinese or English
- **GEE integration** — ready-to-use Google Earth Engine code examples
- **Product comparison** — compare two products side-by-side
- **Download info** — multiple download methods and citations

## Quick Start

```bash
# Search
python scripts/modis_products.py search NDVI
python scripts/modis_products.py search 植被指数

# Show details
python scripts/modis_products.py show MOD13Q1

# GEE code example
python scripts/modis_products.py gee MOD13Q1

# List by category
python scripts/modis_products.py category vegetation_indices

# Database statistics
python scripts/modis_products.py stats
```

## Product Categories

| Category | Products |
|----------|----------|
| Vegetation Indices | 12 (MOD13 series) |
| Surface Reflectance | 5 (MOD09 series) |
| Land Surface Temperature | 4 (MOD11 series) |
| Land Cover | 2 (MCD12 series) |
| Thermal Anomalies / Fire | 4 (MOD14 series) |
| Snow Cover | 3 (MOD10 series) |
| ... | ... |

## License

MIT-0
