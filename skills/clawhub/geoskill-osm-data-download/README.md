# osm-data-download

Download OpenStreetMap features via Overpass API by bbox and tag filter.

## Features

- Download roads, buildings, POIs, landuse, natural features
- Custom Overpass QL queries
- GeoJSON and Shapefile output
- Built-in rate limiting

## Installation

### Option 1: ClawHub
```bash
clawhub install osm-data-download
```

### Option 2: Manual
```bash
git clone https://github.com/ruiduobao/osm-data-download.git
cd osm-data-download
pip install -r requirements.txt
```

### Option 3: Claude Code / skills.sh
```bash
claude skills install osm-data-download
```

## Quick Start

```bash
python scripts/osm-data-download.py download \
  --bbox "116.0,39.5,116.8,40.2" --feature highway \
  -o roads.geojson

python scripts/osm-data-download.py download \
  --bbox "116.3,39.8,116.5,40.0" --feature building \
  -o buildings.geojson

python scripts/osm-data-download.py list-tags
```

## Dependencies

```
requests>=2.28.0
tqdm>=4.64.0
fiona>=1.8.0    (optional, for Shapefile output)
shapely>=1.8.0  (optional, for Shapefile output)
```

## Data Source

OpenStreetMap via Overpass API. Data © OpenStreetMap contributors (ODbL).

## License

MIT-0 (Public Domain)

---

# 中文说明

通过 Overpass API 下载 OpenStreetMap 数据。

## 功能

- 下载道路、建筑、POI、土地利用、自然地物
- 自定义 Overpass QL 查询
- GeoJSON 和 Shapefile 输出
- 内置速率限制

## 安装

### 方式一：ClawHub
```bash
clawhub install osm-data-download
```

### 方式二：手动安装
```bash
git clone https://github.com/ruiduobao/osm-data-download.git
cd osm-data-download
pip install -r requirements.txt
```

### 方式三：Claude Code / skills.sh
```bash
claude skills install osm-data-download
```

## 快速开始

```bash
python scripts/osm-data-download.py download \
  --bbox "116.0,39.5,116.8,40.2" --feature highway \
  -o roads.geojson

python scripts/osm-data-download.py download \
  --bbox "116.3,39.8,116.5,40.0" --feature building \
  -o buildings.geojson

python scripts/osm-data-download.py list-tags
```

## 数据来源

OpenStreetMap via Overpass API. 数据 © OpenStreetMap contributors (ODbL)。

## 许可证

MIT-0 (Public Domain)
