# forest-carbon-estimate

**Forest Carbon Stock Estimator** — BEF, Allometric, IPCC methods with uncertainty analysis.

## Install

### ClawHub
```bash
clawhub install forest-carbon-estimate
```

### Manual
```bash
git clone https://github.com/ruiduobao/forest-carbon-estimate.git
cd forest-carbon-estimate
pip install -r requirements.txt  # numpy, rasterio (for raster mode)
```

### Claude Code / skills.sh
```bash
/clawhub install forest-carbon-estimate
```

## Quick Start
```bash
python scripts/forest-carbon-estimate.py estimate --method allometric --height 15 --forest-type tropical
python scripts/forest-carbon-estimate.py estimate --input height.tif --method allometric --output carbon.tif
python scripts/forest-carbon-estimate.py uncertainty --method allometric --height 15 --iterations 5000
```

## Data Source
- IPCC Guidelines for National Greenhouse Gas Inventories (2006, 2019 Refinement)

## License
MIT-0

---

# 森林碳储量估算工具

**森林碳储量估算器** — 支持 BEF、异速生长方程、IPCC 方法，含不确定性分析。

## 安装

### 手动安装
```bash
git clone https://github.com/ruiduobao/forest-carbon-estimate.git
cd forest-carbon-estimate
pip install numpy rasterio
```

## 快速开始
```bash
python scripts/forest-carbon-estimate.py estimate --method allometric --height 15 --forest-type tropical
python scripts/forest-carbon-estimate.py estimate --input height.tif --method allometric --output carbon.tif
python scripts/forest-carbon-estimate.py uncertainty --method allometric --height 15 --iterations 5000
```

## 数据来源
- IPCC 国家温室气体清单指南（2006，2019 修订）

## 许可证
MIT-0
