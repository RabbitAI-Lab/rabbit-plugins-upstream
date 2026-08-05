---
name: geoskill-ecological-corridor-design
description: '由栖息地适宜性构建阻力面，Dijkstra 最小成本路径识别生态廊道，并计算 PC 景观连通性指数。Designs ecological corridors with least-cost paths and connectivity indices. 输出阻力面与廊道 GeoTIFF + 参数 JSON。'
---

# 生态廊道设计 | Ecological Corridor Design

The resistance surface is computed as (1 − suitability) × 100 + 1; source–sink least-cost paths are solved on a 4-connected raster graph with scipy.sparse.csgraph.dijkstra (automatically bypassing high-resistance bands), and the corridor raster is generated according to the buffer width; the PC connectivity index is the sum of squared area proportions of connected patches, measuring overall landscape connectivity (a single large patch > fragmented small patches).

Use cases: connectivity analysis of ecological conservation red lines, wildlife migration corridor planning, and urban greenway route selection.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Example 1: synthetic two-patch + corridor scenario

```bash
python geoskill-ecological-corridor-design.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: real suitability raster

```bash
python geoskill-ecological-corridor-design.py --input suitability.tif --output-dir ./real
```

### Example 3: wider corridor buffer

```bash
python geoskill-ecological-corridor-design.py --bbox 116 39 117 40 --synthetic --buffer 4 --output-dir ./wide
```

### Example 4: adjusting the PC threshold

```bash
python geoskill-ecological-corridor-design.py --bbox 121 31 122 32 --synthetic --pc-threshold 0.6 --output-dir ./pc06
```

### Example 5: silent batch run

```bash
python geoskill-ecological-corridor-design.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `resistance_surface.tif` | GeoTIFF (float32) | Resistance surface [1,101], EPSG:4326 |
| `corridor.tif` | GeoTIFF (float32) | Corridor raster (1 = corridor) |
| `corridor_params.json` | JSON | Source/sink pixels, path length, total cost, PC index |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (habitat suitability, optional); least-cost path and the PC index are published landscape-ecology methods; synthetic mode generates a two-patch scenario locally with no external data sources.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-ecological-corridor-design
description: '由栖息地适宜性构建阻力面，Dijkstra 最小成本路径识别生态廊道，并计算 PC 景观连通性指数。Designs ecological corridors with least-cost paths and connectivity indices. 输出阻力面与廊道 GeoTIFF + 参数 JSON。'
---

# 生态廊道设计 | Ecological Corridor Design

阻力面 = (1 - 适宜性)×100 + 1；在 4-邻域栅格图上用 scipy.sparse.csgraph.dijkstra 求源-汇最小成本路径（自动绕开高阻力带），按缓冲宽度生成廊道栅格；PC 连通性指数 = 各连通斑块面积占比平方和，度量景观整体连通度（单一大斑块 > 破碎化小斑块）。

适用场景：生态保护红线连通性分析、野生动物迁徙廊道规划、城市绿道选线。

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 示例 1：合成双斑块+走廊场景

```bash
python geoskill-ecological-corridor-design.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实适宜性栅格

```bash
python geoskill-ecological-corridor-design.py --input suitability.tif --output-dir ./real
```

### 示例 3：更宽廊道缓冲

```bash
python geoskill-ecological-corridor-design.py --bbox 116 39 117 40 --synthetic --buffer 4 --output-dir ./wide
```

### 示例 4：调整 PC 阈值

```bash
python geoskill-ecological-corridor-design.py --bbox 121 31 122 32 --synthetic --pc-threshold 0.6 --output-dir ./pc06
```

### 示例 5：静默批量

```bash
python geoskill-ecological-corridor-design.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `resistance_surface.tif` | GeoTIFF (float32) | 阻力面 [1,101]，EPSG:4326 |
| `corridor.tif` | GeoTIFF (float32) | 廊道栅格（1=廊道） |
| `corridor_params.json` | JSON | 源/汇像元、路径长度、总成本、PC 指数 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（栖息地适宜性，可选）；最小成本路径与 PC 指数为景观生态学公开方法；合成模式本地生成双斑块场景，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
