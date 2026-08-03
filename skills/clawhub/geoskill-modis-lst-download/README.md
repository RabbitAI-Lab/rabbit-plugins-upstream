# MODIS Land Surface Temperature Download

## English

Search and download MODIS LST products from NASA LAADS DAAC.

### Installation

**ClawHub:**
```bash
clawhub install modis-lst-download
```

**Claude Code / skills.sh:**
```bash
claude skills install modis-lst-download
```

**Manual:**
```bash
git clone <repo-url> modis-lst-download
cd modis-lst-download
pip install requests tqdm
```

### Quick Start

```bash
# Search for available data
python scripts/modis_lst_download.py search \
  --product MOD11A1 \
  --start 2023-06-01 --end 2023-06-30 \
  --bbox 116.0 39.5 116.8 40.2

# Configure Earthdata credentials
python scripts/modis_lst_download.py configure --username your_username

# Download data
python scripts/modis_lst_download.py download \
  --product MOD11A1 \
  --start 2023-07-01 --end 2023-07-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --output ./lst_data/
```

### Authentication

NASA Earthdata requires a free account. Register at https://urs.earthdata.nasa.gov/

### Data Source

- **API**: NASA LAADS DAAC (https://ladsweb.modaps.eosdis.nasa.gov/)
- **License**: Public Domain (NASA open data)
- **Citation**: Wan, Z., S. Hook, and G. Hulley, 2015. MOD11A2 MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006.

---

## 中文

从 NASA LAADS DAAC 搜索和下载 MODIS 地表温度产品。

### 安装

**ClawHub:**
```bash
clawhub install modis-lst-download
```

**Claude Code / skills.sh:**
```bash
claude skills install modis-lst-download
```

**手动安装:**
```bash
git clone <repo-url> modis-lst-download
cd modis-lst-download
pip install requests tqdm
```

### 快速开始

```bash
# 搜索可用数据
python scripts/modis_lst_download.py search \
  --product MOD11A1 \
  --start 2023-06-01 --end 2023-06-30 \
  --bbox 116.0 39.5 116.8 40.2

# 配置 Earthdata 认证
python scripts/modis_lst_download.py configure --username your_username

# 下载数据
python scripts/modis_lst_download.py download \
  --product MOD11A1 \
  --start 2023-07-01 --end 2023-07-01 \
  --bbox 116.0 39.5 116.8 40.2 \
  --output ./lst_data/
```

### 认证说明

NASA Earthdata 需要免费账号。请在 https://urs.earthdata.nasa.gov/ 注册。

### 数据来源

- **API**: NASA LAADS DAAC (https://ladsweb.modaps.eosdis.nasa.gov/)
- **许可证**: 公共领域（NASA 开放数据）
- **引用**: Wan, Z., S. Hook, and G. Hulley, 2015. MOD11A2 MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V006.
