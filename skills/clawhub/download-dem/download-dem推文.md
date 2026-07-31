# 锐多宝：DEM下载skill（download-dem）

做GIS项目时，下载DEM数据是一个高频需求。每次都要经历：找数据源 → 注册账号 → 手动框选范围 → 下载瓦片 → 拼接 → 裁剪 → 验证。一个县的30m DEM，走完这套流程少说半小时。

更麻烦的是大面积任务。下载到一半断了，从头再来；不同数据源的高程基准不统一，拼出来的数据有台阶；瓦片重叠区域出现拼接缝……这些问题反复消耗时间。

为了解决这些问题，我开发了 **download-dem** 这个skill。它不是简单的下载脚本，而是一套覆盖「规划 → 检索 → 传输 → 拼接 → 验证 → 溯源」全流程的确定性工具。

> 项目地址：<https://clawhub.ai/ruiduobao/skills/download-dem>
>
> Microsoft Planetary Computer STAC API：<https://planetarycomputer.microsoft.com/api/stac/v1>
>
> AWS Open Data Copernicus DEM：<https://registry.opendata.aws/copernicus-dem/>

---

## 一、为什么不能只靠手动下载？

通用做法的痛点不在于"能不能下到数据"，而在于过程中的不确定性：

- **数据源选择**：Copernicus GLO-30、SRTM、NASADEM、AW3D30、ASTER GDEM……用哪个？它们的表面类型（DSM还是DEM）、垂直基准（EGM96还是EGM2008）、分辨率、覆盖范围各不相同。混用会导致高程不一致。
- **大面积任务**：一个省的30m DEM涉及几十个瓦片，几百GB数据。全部读入内存拼接会崩溃；中断后无法续传只能重来。
- **数据完整性**：下载的瓦片有没有损坏？CRS是否正常？范围是否真的覆盖了研究区？NoData占比多少？不做验证就敢用的数据，下游分析全错。
- **可复现性**：别人拿到你的结果，能追溯到你用了哪个数据源、哪个版本、哪个范围吗？

download-dem的做法是：**用确定性程序处理这些工程问题，把数据源选择、传输策略、完整性校验全部固化下来。**

---

## 二、开发原理

### 1. 整体架构：plan → download → validate 三步走

整个skill的核心是一个Python脚本 `dem_download.py`，提供三个子命令：

```text
plan      → 规划：确定数据源、数据集、输出模式、资源估算
download  → 执行：检索资产、传输、拼接/存瓦片、写溯源
validate  → 验证：检查CRS、尺寸、NoData、统计、范围重叠
```

每一步输出结构化JSON，下一步可以直接消费。这不是一个"一键下载"的黑盒，而是一个可审计、可中断、可复现的工程流程。

### 2. 数据源：五大渠道，自动选择

skill内置了五个数据源的适配器：

| 数据源 | 数据集 | 分辨率 | 表面类型 | 垂直基准 | 认证 |
|---|---|---:|---|---|---|
| MPC（Microsoft Planetary Computer） | Copernicus GLO-30/90 | 30/90 m | DSM | EGM2008 | 运行时签名，无需密钥 |
| AWS Open Data | Copernicus GLO-30/90 | 30/90 m | DSM | EGM2008 | 匿名HTTPS |
| OpenTopography | SRTM/NASADEM/AW3D30/COP30等 | 30-450 m | 混合 | EGM96/椭球 | 需API Key |
| USGS 3DEP | 10m/1m | 10/1 m | 裸地DEM | NAVD88等 | 公共API |
| NASA Earthdata | ASTER GDEM V3 | 30 m | DSM | EGM96 | 需Token |

`--source auto` 时，默认选择MPC的Copernicus GLO-30（全球30m DSM，EGM2008基准）。如果MPC失败且尚无已完成资产，自动回退到AWS直接匿名访问。

数据源选择不是随便挑的。每个适配器都对接了官方API：
- MPC通过STAC API + `planetary_computer.sign_inplace` 做运行时签名检索
- AWS直接构造一-degree COG的S3对象路径匿名读取
- OpenTopography调用Global DEM API，按地理范围分块请求
- USGS调用TNM Access API分页检索
- Earthdata通过CMR Granule API检索 `ASTGTM.003` 集合

### 3. 输出模式：自动判断 mosaic 还是 tiles

这是设计中最关键的决策之一。skill用两个独立指标判断：

- **AOI面积**：矢量几何面积优先，无矢量时用bbox球面面积
- **bbox像元数**：按目标分辨率在完整bbox矩形上的像元总数（因为拼接出的GeoTIFF是矩形，即使AOI是稀疏的）

默认 `--mode auto` 的规则：

```text
面积 ≤ 10,000 km² 且 像元 ≤ 1 亿  →  windowed mosaic（窗口化拼接）
面积 > 10,000 km² 或 像元 > 1 亿  →  tiles（原始瓦片目录）
```

为什么要这么设计？因为一个省级30m DEM可能有几十GB，全部读入内存拼接不现实。而一个县级DEM只有几MB，直接拼接成单个GeoTIFF更方便下游使用。

### 4. 窗口化拼接：受控内存，不爆内存

mosaic模式的核心是 `rasterio.merge.merge()`，但关键在于参数：

```python
merge(
    datasets,
    bounds=tuple(bbox),          # 限定到bbox范围
    nodata=nodata,
    target_aligned_pixels=True,  # 像元对齐
    mem_limit=mem_limit_mb,      # 内存上限（默认256MB）
    dst_path=temporary,          # 直接写临时文件，不分配整个数组
    dst_kwds={
        "driver": "GTiff",
        "compress": "DEFLATE",   # LZW/DEFLATE压缩
        "tiled": True,           # 分块存储
        "blockxsize": 512,
        "blockysize": 512,
        "BIGTIFF": "IF_SAFER",   # 自动启用BigTIFF
    },
)
```

`mem_limit` 参数让rasterio在受控内存窗口内分块写入，而不是一次性分配整个拼接数组。拼接完成后，临时文件原子替换为目标文件——如果中途失败，不会留下半个损坏的文件。

### 5. 远程COG流式读取：不下载就能拼接

对于MPC和AWS的Copernicus DEM，源数据本身就是COG（Cloud Optimized GeoTIFF）。skill默认不做本地下载，而是通过GDAL/rasterio的HTTP range read直接流式读取远程COG的窗口数据。

这意味着：**一个县级30m DEM，不需要先下载几个GB的原始瓦片到本地，而是直接从云端读取需要的窗口，拼接成最终结果。** 传输量等于最终输出的大小，不是原始瓦片的总大小。

如果流式读取失败（网络问题等），skill会自动回退到本地暂存模式：先续传下载所有资产到本地，再在本地拼接。

### 6. 断点续传：中断不丢数据

大任务最怕中断。skill的续传机制：

- 每个资产下载到 `.part` 文件，完成后原子重命名为最终文件名
- 支持 HTTP Range 请求：中断后重跑同一命令，已下载部分继续，不从头开始
- `manifest.json` 记录每个资产的状态（pending/downloading/completed/failed）、字节数、SHA-256
- 重跑时已完成资产（字节数匹配）直接跳过
- `--verify-existing` 可以在跳过前先做SHA-256校验，防止静默损坏

```text
<output>/
  dem-job.json          ← 任务级元数据
  <provider>/
    manifest.json        ← 资产清单（状态、字节数、SHA-256）
    source-file-1.tif    ← 已完成
    source-file-2.part   ← 中断的半成品，下次继续
```

### 7. 安全设计：不泄露密钥

DEM数据源中，OpenTopography需要API Key，NASA Earthdata需要Token。skill的安全规则：

- `safe_error()` 函数在错误信息中自动脱敏：API Key、Token、Authorization头、签名URL参数全部替换为 `<redacted>`
- `clean_url()` 在溯源文件中只保存去掉查询参数的脱敏URL
- manifest中绝不持久化签名参数、Token或Authorization头

### 8. 验证：不盲信下载结果

验证不是可选步骤。`validate` 命令检查：

- CRS是否存在
- 栅格尺寸是否有效
- 采样像元中是否有有效值
- 统计量（min/max/mean）是否有限
- 输出范围是否与请求bbox重叠
- NoData占比
- 瓦片模式下还可做 `--verify-checksums` 全量SHA-256审计

### 9. 溯源：JSON sidecar记录一切

每次download完成后，输出文件旁会生成一个 `.dem.json` 溯源文件，记录：

```json
{
  "source": "mpc",
  "dataset": "cop-dem-glo-30",
  "mode": "mosaic",
  "bbox_wgs84": [104.78, 30.05, 105.30, 30.55],
  "surface": "DSM",
  "vertical_datum": "EGM2008",
  "provider": {
    "asset_count": 2,
    "assets": ["脱敏URL1", "脱敏URL2"],
    "transfer": "remote_cog_windowed"
  },
  "validation": { "status": "pass", ... }
}
```

别人拿到你的GeoTIFF，打开sidecar就能知道数据从哪来、什么基准、怎么处理的。

---

## 三、实测：下载四川省资阳市乐至县30m DEM

### 第一步：规划

```bash
python scripts/dem_download.py plan \
  --bbox 104.78 30.05 105.30 30.55 \
  --source auto --dataset cop-dem-glo-30 --mode auto
```

输出：

```json
{
  "source": "mpc",
  "dataset": "cop-dem-glo-30",
  "bbox_wgs84": [104.78, 30.05, 105.30, 30.55],
  "aoi_area_km2": 2775.575,
  "estimated_pixels_for_bbox_grid": 3369600,
  "estimated_asset_count": 2,
  "selected_mode": "mosaic",
  "mode_reason": "within_area_and_pixel_limits",
  "resolution_m": 30,
  "surface": "DSM",
  "vertical_datum": "EGM2008",
  "credentials": "Runtime asset signing; no user key for public catalog access"
}
```

面积2775km²，像元337万，远低于限制 → 自动选择mosaic模式。只需2个Copernicus瓦片，无需任何密钥。

### 第二步：下载

```bash
python scripts/dem_download.py download \
  --bbox 104.78 30.05 105.30 30.55 \
  --source auto --dataset cop-dem-glo-30 --mode auto \
  --output lezhi_dem_30m.tif --workers 4
```

执行过程（stderr事件流）：

```text
discover_start    → source=mpc, dataset=cop-dem-glo-30
discover_complete → assets=2（耗时3.3秒）
mosaic_start      → sources=2, mem_limit_mb=256
mosaic_complete   → output=lezhi_dem_30m.tif, bytes=10912700（耗时95秒）
```

2个远程COG瓦片通过HTTP range read流式读取，窗口化拼接写入本地GeoTIFF。全程没有下载任何原始瓦片到本地。

### 第三步：验证

```bash
python scripts/dem_download.py validate lezhi_dem_30m.tif \
  --bbox 104.78 30.05 105.30 30.55
```

输出：

```json
{
  "status": "pass",
  "crs": "EPSG:4326",
  "bounds": [104.78, 30.05, 105.30, 30.55],
  "width": 1872,
  "height": 1800,
  "dtype": "float32",
  "nodata": -9999.0,
  "resolution": [0.00027778, 0.00027778],
  "valid_sampled_pixels": 1048576,
  "nodata_fraction_sample": 0.0,
  "statistics_sample": {
    "min": 290.43,
    "max": 593.68,
    "mean": 411.60
  },
  "requested_bbox_overlap": true,
  "failures": [],
  "warnings": []
}
```

验证通过。1872×1800像元，float32，EPSG:4326，0% NoData。乐至县地处四川盆地丘陵区，高程范围290-594m，均值412m，与实际地形吻合。

### 最终交付

```text
lezhi_dem_30m.tif          11 MB   ← 拼接后的DEM
lezhi_dem_30m.tif.dem.json 1.9 KB ← 溯源文件
```

从规划到验证完成，总耗时约2分钟。全程零手动操作。

---

## 四、更多用法

### 1. 用矢量AOI精确裁剪

bbox是矩形，如果你有行政边界矢量文件，可以用 `--aoi` 代替 `--bbox`：

```bash
python scripts/dem_download.py download \
  --aoi lezhi_boundary.geojson \
  --source auto --dataset cop-dem-glo-30 --mode auto \
  --output lezhi_dem_masked.tif
```

mosaic模式下，skill会先拼接bbox矩形，然后按矢量边界做分块掩膜（block-wise mask）——逐个内部栅格块判断是否在AOI内，不在的设为NoData。不会一次性分配整个掩膜数组。

### 2. 90m分辨率（更小文件）

```bash
python scripts/dem_download.py download \
  --bbox 104.78 30.05 105.30 30.55 \
  --source auto --dataset cop-dem-glo-90 --mode auto \
  --output lezhi_dem_90m.tif
```

### 3. 大面积任务（瓦片模式）

当面积超过10,000km²或像元超过1亿时，自动切换到tiles模式：

```bash
python scripts/dem_download.py download \
  --aoi sichuan_province.geojson \
  --source auto --dataset cop-dem-glo-30 --mode auto \
  --output sichuan_tiles --workers 6
```

输出的是原始瓦片目录，不拼接、不裁剪。中断后重跑同一命令即可续传：

```text
sichuan_tiles/
  dem-job.json
  mpc/
    manifest.json
    Copernicus_DSM_COG_10_N28_00_E102_00_DEM.tif
    Copernicus_DSM_COG_10_N29_00_E103_00_DEM.tif.part  ← 中断的，下次继续
    ...
```

### 4. SRTM数据（通过OpenTopography）

```bash
export OPENTOPOGRAPHY_API_KEY=your_key
python scripts/dem_download.py download \
  --bbox 104.78 30.05 105.30 30.55 \
  --source opentopography --dataset SRTMGL1 --mode auto \
  --output lezhi_srtm.tif
```

### 5. ASTER GDEM V3（通过NASA Earthdata）

```bash
export EARTHDATA_TOKEN=your_token
python scripts/dem_download.py download \
  --bbox 104.78 30.05 105.30 30.55 \
  --source earthdata --dataset aster-gdem-v3 --mode auto \
  --output lezhi_aster.tif
```

### 6. 验证已有瓦片目录

```bash
python scripts/dem_download.py validate sichuan_tiles --verify-checksums
```

对manifest中每个资产做SHA-256全量校验，确保没有静默损坏。

---

## 五、关键设计取舍

### 为什么默认用Copernicus GLO-30而不是SRTM？

Copernicus DEM（2021年发布）的精度和时效性优于SRTM（2000年采集）。GLO-30全球覆盖完整，包括高纬度地区（SRTM只覆盖60°N-56°S）。而且MPC上的Copernicus数据是COG格式，支持远程窗口读取，不需要下载整个瓦片。

### 为什么不自动填空洞、不重采样？

skill的数据完整性原则是：**保留原始值。** 除非用户明确要求并记录，否则不填洞、不平滑、不重采样、不派生地形产品。每一个操作都应该是有意识的决策，不是黑盒里的默认行为。

### 为什么不混用不同数据源？

不同数据源的垂直基准不同（EGM96 vs EGM2008），表面类型不同（DSM vs DEM），采集时间不同。混用会导致拼接处出现高程台阶。skill明确禁止混用不同数据源的部分瓦片，除非有文档化的垂直基准转换。

---

## 六、写在最后

DEM下载看起来简单，但要做好需要处理大量工程细节：数据源选择、COG流式读取、内存控制、断点续传、完整性校验、密钥安全、溯源记录。

download-dem把这些全部固化成一个确定性流程。你只需要提供一个bbox或矢量AOI，剩下的交给程序：

- 自动选择最优数据源
- 自动判断拼接还是存瓦片
- 自动流式读取或续传下载
- 自动验证并生成溯源文件

> skill入口：
> - ClawHub：<https://clawhub.ai/ruiduobao/skills/download-dem>

---

## 参考来源

注：本文的skill思路由锐多宝提出，skill代码和该博客由AI辅助完成。

1. Microsoft Planetary Computer Copernicus DEM GLO-30：<https://planetarycomputer.microsoft.com/dataset/cop-dem-glo-30>
2. AWS Open Data Copernicus DEM Registry：<https://registry.opendata.aws/copernicus-dem/>
3. OpenTopography API Documentation：<https://portal.opentopography.org/apidocs/>
4. USGS 3D Elevation Program：<https://www.usgs.gov/3d-elevation-program>
5. NASA Earthdata ASTER GDEM V3：<https://doi.org/10.5067/ASTER/ASTGTM.003>
6. Copernicus DEM Product Handbook：通过AWS Registry入口获取
7. download-dem ClawHub：<https://clawhub.ai/ruiduobao/skills/download-dem>
