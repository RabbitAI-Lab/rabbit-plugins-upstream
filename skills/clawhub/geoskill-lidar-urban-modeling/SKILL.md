---
name: geoskill-lidar-urban-modeling
description: 'LiDAR点云地面滤波生成nDSM，连通域+矢量化提取建筑轮廓并估算高度与体积'
---

# LiDAR 城市三维建模 | LiDAR Urban 3D Modeling

Extracts urban buildings from a LiDAR point cloud and builds 2.5D models (footprints + height + volume). Workflow:

1. **Ground filtering**: rasterize the minimum-elevation surface (or the 10th-percentile surface) and apply Progressive Morphological Filtering (PMF, a simplified version of Zhang et al. 2003) with successively larger openings to trim building protrusions and estimate the bare-earth DTM;
2. **nDSM**: subtract the DTM from the maximum-elevation DSM to obtain the Normalized Digital Surface Model (object height above ground);
3. **Building extraction**: threshold the nDSM at ≥ min_height, 8-connected component labeling, and minimum footprint-area filtering;
4. **Vectorization and modeling**: extract polygon footprints per connected component with rasterio.features.shapes, assign each building a height (max/mean nDSM within the region), footprint area (sum of raster cell areas), and volume (mean height × footprint area), then write GeoJSON with geopandas.

Synthetic mode generates a simulated point cloud of gentle terrain + several random rectangular buildings (height 6–25 m, footprint 8–18 m, dense rooftop grid points + wall points at multiple heights, no ground returns inside building footprints), automatically matches the ground truth, and reports the detection rate and height RMSE. Suited to urban 3D modeling, building stock estimation, and floor-area-ratio / building-volume analysis.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## Usage / 使用方法

### Basic usage (synthetic data, offline)

```bash
python geoskill-lidar-urban-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1: default 3 m minimum building height

```bash
python geoskill-lidar-urban-modeling.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --min-height 3.0 \
    --output-dir ./bld_3m
```

### Example 2: percentile ground + large-area filter (large buildings only)

```bash
python geoskill-lidar-urban-modeling.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --ground-method percentile --min-area 50 \
    --output-dir ./bld_large
```

### Example 3: real point cloud input (.npy / .csv / .txt xyz)

```bash
python geoskill-lidar-urban-modeling.py \
    --input city_block.npy --min-height 3.0 --cell-size 1.0 \
    --output-dir ./real_block
```

### Example 4: low-rise structure inventory (lower threshold + small area)

```bash
python geoskill-lidar-urban-modeling.py \
    --input city_block.csv --min-height 1.5 --min-area 6 --quiet \
    --output-dir ./sheds
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `ndsm.tif` | GeoTIFF (float32) | Normalized Digital Surface Model, EPSG:4326 |
| `buildings.geojson` | GeoJSON (Polygon) | Building footprints + height_max/height_mean/area/volume attributes |
| `stats.json` | JSON | Building count, height/volume statistics, detection rate and RMSE (synthetic mode) |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

- **Real mode**: local point cloud files (.npy / .csv / .txt, at least 3 columns of xyz, projected or local metric coordinates recommended)
- **Synthetic mode**: locally generated point cloud of terrain + rectangular buildings; no external data source

## Privacy / 隐私声明 / Privacy

- Runs fully offline; accesses no network services
- All processing is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-lidar-urban-modeling
description: 'LiDAR点云地面滤波生成nDSM，连通域+矢量化提取建筑轮廓并估算高度与体积'
---

# LiDAR 城市三维建模 | LiDAR Urban 3D Modeling

从 LiDAR 点云提取城市建筑物并构建 2.5D 模型（轮廓 + 高度 + 体积）。
流程：

1. **地面滤波**：最低高程面（或 10% 分位数面）栅格 + 渐进形态学滤波
   PMF（Zhang et al. 2003 简化版）逐级开运算削去建筑突起，估计裸地
   DTM；
2. **nDSM**：最高高程面 DSM 减 DTM，得归一化数字表面模型
   （地物高出地面的高度）；
3. **建筑提取**：nDSM ≥ min_height 阈值化 + 8 连通域标记 + 最小底
   面积过滤；
4. **矢量化建模**：rasterio.features.shapes 逐连通域提取多边形轮廓，
   每栋赋高度（区域内 nDSM 最大/均值）、底面积（栅格像元面积）与
   体积（平均高 × 底面积），geopandas 写出 GeoJSON。

合成模式生成平缓地形 + 若干随机矩形建筑（高 6–25 m、足迹 8–18 m，
屋顶密网格点 + 多高度墙面点，建筑内部无地面回波）的模拟点云，自动
与真值匹配输出检测率与高度 RMSE。适用于城市三维建模、建筑存量估算、
容积率/体量分析。

## 依赖

```bash
pip install numpy rasterio scipy geopandas shapely
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-lidar-urban-modeling.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1：默认 3 m 起提建筑

```bash
python geoskill-lidar-urban-modeling.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --min-height 3.0 \
    --output-dir ./bld_3m
```

### 示例 2：分位数地面 + 大面积过滤（只提大型建筑）

```bash
python geoskill-lidar-urban-modeling.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --ground-method percentile --min-area 50 \
    --output-dir ./bld_large
```

### 示例 3：真实点云输入（.npy / .csv / .txt xyz）

```bash
python geoskill-lidar-urban-modeling.py \
    --input city_block.npy --min-height 3.0 --cell-size 1.0 \
    --output-dir ./real_block
```

### 示例 4：低矮构筑物普查（降阈值 + 小面积）

```bash
python geoskill-lidar-urban-modeling.py \
    --input city_block.csv --min-height 1.5 --min-area 6 --quiet \
    --output-dir ./sheds
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `ndsm.tif` | GeoTIFF (float32) | 归一化数字表面模型，EPSG:4326 |
| `buildings.geojson` | GeoJSON (Polygon) | 建筑轮廓 + height_max/height_mean/area/volume 属性 |
| `stats.json` | JSON | 栋数、高度/体积统计、检测率与 RMSE（合成模式） |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **真实模式**：本地点云文件（.npy / .csv / .txt，至少 3 列 xyz，
  建议投影或局部米制坐标）
- **合成模式**：本地生成地形 + 矩形建筑点云，无外部数据源

## 隐私声明 / Privacy

- 完全离线运行，不访问任何网络服务
- 所有处理在本地完成，不上传任何用户数据

## License

MIT
