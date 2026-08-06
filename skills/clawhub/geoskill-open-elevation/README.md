# Open-Elevation

Query elevation (in meters) for any lat/lon coordinate on Earth using the free,
public [Open-Elevation](https://open-elevation.com/) API. No API key required.

## Install

### ClawHub
```bash
clawhub install open-elevation
```

### Manual
```bash
git clone https://github.com/ruiduobao/open-elevation.git
cd open-elevation
pip install requests tqdm
```

### Claude Code / skills.sh
```bash
claude skills install open-elevation
```

## Quick Start

```bash
# Single point
python scripts/open-elevation.py lookup --lat 39.9042 --lon 116.4074

# Batch from CSV
python scripts/open-elevation.py batch --input coords.csv --output results.csv
```

## Data Source

- **API**: [Open-Elevation](https://open-elevation.com/)
- **Coverage**: Global
- **License**: Public domain

---

# Open-Elevation 高程查询

使用免费的 [Open-Elevation](https://open-elevation.com/) 公开 API 查询任意经纬度的海拔高度（米）。无需 API 密钥。

## 安装

### ClawHub
```bash
clawhub install open-elevation
```

### 手动安装
```bash
git clone https://github.com/ruiduobao/open-elevation.git
cd open-elevation
pip install requests tqdm
```

### Claude Code / skills.sh
```bash
claude skills install open-elevation
```

## 快速开始

```bash
# 单点查询
python scripts/open-elevation.py lookup --lat 39.9042 --lon 116.4074

# 批量查询
python scripts/open-elevation.py batch --input coords.csv --output results.csv
```

## 数据来源

- **API**: [Open-Elevation](https://open-elevation.com/)
- **覆盖范围**: 全球
- **许可证**: 公有领域
