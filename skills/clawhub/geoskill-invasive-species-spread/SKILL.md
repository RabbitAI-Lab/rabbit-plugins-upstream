---
name: geoskill-invasive-species-spread
description: '多时相指数阈值分类检测入侵新增像元，计算面积相对扩散速率，用环境适宜性×距离衰减预测入侵风险。Monitors invasive species spread from multi-temporal classification and risk prediction. 输出新增入侵与风险 GeoTIFF。'
---

# 入侵物种扩散监测 | Invasive Species Spread Monitoring

Two epochs of remote sensing indices are classified by threshold to obtain the t0 presence zone and the t1 newly invaded zone; spread rate r = (A1−A0)/(A0×Δt); risk prediction = environmental suitability × spread accessibility exp(−d/λ), where d is the Euclidean distance to the nearest known invaded pixel (scipy distance transform) and λ is the dispersal scale (default 5 km). Risk ∈ [0,1].

Use cases: dynamic monitoring of invasive alien species (e.g., smooth cordgrass, Canada goldenrod) and priority ranking for prevention and control.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn
```

## Usage / 使用方法

### Example 1: synthetic two-epoch scenario (default 5-year interval)

```bash
python geoskill-invasive-species-spread.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### Example 2: real 3-band input (index_t0, index_t1, suitability)

```bash
python geoskill-invasive-species-spread.py --input invasive_inputs.tif --output-dir ./real
```

### Example 3: stricter threshold + 3-year interval

```bash
python geoskill-invasive-species-spread.py --bbox 116 39 117 40 --synthetic --threshold 0.2 --dt-years 3 --output-dir ./tuned
```

### Example 4: strongly spreading species (large dispersal scale)

```bash
python geoskill-invasive-species-spread.py --bbox 121 31 122 32 --synthetic --dispersal-scale 10000 --output-dir ./strong
```

### Example 5: quiet batch run

```bash
python geoskill-invasive-species-spread.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `new_invasion.tif` | GeoTIFF (float32) | Newly invaded pixels (0/1), EPSG:4326 |
| `invasion_risk.tif` | GeoTIFF (float32) | Invasion risk ∈ [0,1] |
| `invasive_params.json` | JSON | Area change, spread rate, and risk statistics |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

Local GeoTIFF (3 bands: two-epoch indices + suitability, optional); synthetic mode generates expanding invasion patches and an environmental suitability gradient locally, with no external data source.

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default; makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; no user data is uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-invasive-species-spread
description: '多时相指数阈值分类检测入侵新增像元，计算面积相对扩散速率，用环境适宜性×距离衰减预测入侵风险。Monitors invasive species spread from multi-temporal classification and risk prediction. 输出新增入侵与风险 GeoTIFF。'
---

# 入侵物种扩散监测 | Invasive Species Spread Monitoring

两期遥感指数按阈值分类得到 t0 存在区与 t1 新增入侵区；扩散速率 r = (A1-A0)/(A0×Δt)；风险预测 = 环境适宜性 × 扩散可达性 exp(-d/λ)，其中 d 为到最近已知入侵像元的欧氏距离（scipy 距离变换），λ 为扩散尺度（默认 5 km）。风险 ∈ [0,1]。

适用场景：外来入侵物种（如互花米草、加拿大一枝黄花）动态监测与防控优先级排序。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn
```

## 使用方法

### 示例 1：合成两期场景（默认 5 年间隔）

```bash
python geoskill-invasive-species-spread.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./output
```

### 示例 2：真实 3 波段输入（index_t0,index_t1,suitability）

```bash
python geoskill-invasive-species-spread.py --input invasive_inputs.tif --output-dir ./real
```

### 示例 3：更严阈值 + 3 年间隔

```bash
python geoskill-invasive-species-spread.py --bbox 116 39 117 40 --synthetic --threshold 0.2 --dt-years 3 --output-dir ./tuned
```

### 示例 4：强扩散物种（大扩散尺度）

```bash
python geoskill-invasive-species-spread.py --bbox 121 31 122 32 --synthetic --dispersal-scale 10000 --output-dir ./strong
```

### 示例 5：静默批量

```bash
python geoskill-invasive-species-spread.py --bbox 113 23 114 24 --synthetic --quiet --output-dir ./batch
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `new_invasion.tif` | GeoTIFF (float32) | 新增入侵像元（0/1），EPSG:4326 |
| `invasion_risk.tif` | GeoTIFF (float32) | 入侵风险 ∈ [0,1] |
| `invasive_params.json` | JSON | 面积变化、扩散速率、风险统计 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

本地 GeoTIFF（3 波段两期指数+适宜性，可选）；合成模式本地生成扩张型入侵斑块与环境适宜性梯度，无外部数据源。

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
