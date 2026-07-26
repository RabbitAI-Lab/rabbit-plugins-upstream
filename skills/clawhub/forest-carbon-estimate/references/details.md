
默认：0.55 g/cm³。使用 `--wood-density` 覆盖。

## 方法选择指南

| 方法 | 适用场景 | 所需输入 |
|------|----------|----------|
| BEF | 森林资源清查数据 | AGB (t/ha) |
| 异速生长 | 遥感（LiDAR/InSAR 树高） | 树高 (m) |
| IPCC Tier 1 | 快速估算，无野外数据 | 森林类型 + 面积 |

## 输出单位

碳储量以 **Mg C/ha**（兆克碳/公顷）报告，等同于 **t C/ha**。

总储量：乘以面积（ha）→ 总 Mg C。

## NoData 处理

输入栅格中的 NoData 像元被跳过。输出 GeoTIFF 使用与输入相同的 nodata 值。不对 NoData 区域进行插值。

## 自定义参数

```bash
# 自定义碳分数和根冠比
python scripts\forest-carbon-estimate.py estimate --method bef --agb 200 --forest-type temperate --carbon-fraction 0.45 --root-shoot-ratio 0.28
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--carbon-fraction` | 0.47 | 干生物量碳分数 |
| `--root-shoot-ratio` | 0.26 | 根冠比 |
| `--bef` | 1.32 | 生物量扩展因子 |

## 不确定性输出结构

```json
{
  "mean": 125.3,
  "std": 18.7,
  "CI95_lower": 88.6,
  "CI95_upper": 162.0
}
```

| 字段 | 说明 |
|------|------|
| `mean` | 碳储量估算均值 (Mg C/ha) |
| `std` | 蒙特卡洛标准差 |
| `CI95_lower` | 95% 置信区间下界 |
| `CI95_upper` | 95% 置信区间上界 |

## 数据获取指南

从以下渠道获取森林树高/AGB 栅格：
- **Global Forest Watch** (https://www.globalforestwatch.org/) — AGB 地图
- **NASA GEDI** (https://gedi.umd.edu/) — 星载 LiDAR 森林树高
- **ESA Biomass Mission** — P 波段 SAR 森林树高
- **国家森林资源清查** — 样地 AGB 数据

## 验证/质量评估

- 与野外实测碳储量样地对比
- 用同森林类型 IPCC 默认值交叉验证
- 检查不确定性范围（CI95）是否合理（< 均值的 50%）
- 在论文中报告方法、森林类型和输入数据来源

## 引用格式

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

## 可视化指南

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
cbar.set_label("碳储量 (Mg C/ha)")
ax.set_title("森林碳储量")
ax.axis("off")
plt.tight_layout()
plt.savefig("carbon_map.png", dpi=200)
```

## 故障排除

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `ConnectionError` | 网络问题 | 检查网络，重试 |
| `HTTP 429` | 速率限制 | 等待 60 秒后重试 |
| `ValueError` | 无效输入 | 检查参数格式 |
| 空输出 | 无数据 | 尝试不同参数 |
| `ModuleNotFoundError` | 缺少依赖 | 运行 pip install |

基于遥感数据估算森林碳储量，支持 BEF、异速生长方程、IPCC Tier 1/2 三种方法，含蒙特卡洛不确定性分析。

## 功能特性

- **BEF 法**：生物量扩展因子从地上生物量推算
- **异速生长方程**：AGB = a × H^b，从树高推算
- **IPCC Tier 1/2**：按森林类型的默认因子
- **蒙特卡洛不确定性**：输入不确定性传播分析
- **栅格处理**：直接输入输出 GeoTIFF
- **表格处理**：CSV 样地数据
- **多森林类型**：热带、温带、寒带、红树林

## 使用方法

```bash
# 单点估算（异速生长）
python scripts\forest-carbon-estimate.py estimate --method allometric --height 15 --forest-type tropical

# 单点估算（BEF）
python scripts\forest-carbon-estimate.py estimate --method bef --agb 200 --forest-type temperate

# IPCC Tier 1 默认值
python scripts\forest-carbon-estimate.py estimate --method ipcc --forest-type boreal --area-ha 100

# 栅格处理
python scripts\forest-carbon-estimate.py estimate --input height.tif --method allometric --output carbon.tif

# 不确定性分析
python scripts\forest-carbon-estimate.py uncertainty --method allometric --height 15 --iterations 5000

# 从 CSV 生成报告
python scripts\forest-carbon-estimate.py report --input carbon_stock.csv
```

## 计算链

```
AGB（地上生物量）
  ↓
BGB = AGB × 根冠比（默认 0.26）
  ↓
总生物量 = AGB + BGB
  ↓
碳储量 = 总生物量 × 碳分数（默认 0.47）
```

## 方法对比

| 方法 | 输入 | 说明 |
|------|------|------|
| BEF | AGB (t/ha) | 总生物量 = AGB × BEF |
| 异速生长 | 树高 (m) | AGB = a × H^b |
| IPCC | 森林类型 | IPCC 默认密度 |

## 数据来源

- IPCC 国家温室气体清单指南（2006，2019 修订）
- IPCC EFDB（排放因子数据库）
