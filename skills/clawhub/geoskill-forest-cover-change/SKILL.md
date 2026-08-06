---
name: geoskill-forest-cover-change
description: '多期 NDVI 阈值与变化矢量幅度检测森林损失/增益/稳定，输出变化栅格与年度面积统计'
---

# 森林覆盖变化检测 | Forest Cover Change Detection

Detects forest loss / gain / stable from multi-temporal NDVI. For each period, an NDVI threshold (default 0.3) classifies forest pixels; comparing the first and last periods, a pixel changing from forest to non-forest with a drop ≥ the drop threshold is recorded as loss, a pixel changing from non-forest to forest with an increase ≥ the gain threshold is recorded as gain, and everything else is recorded as stable. The change vector magnitude (CVA, the L2 norm of the adjacent-period difference) is also computed to quantify change intensity.

Typical applications: deforestation monitoring, afforestation effectiveness assessment, and annual forest resource change ledgers. In synthetic mode, logging (loss) and afforestation (gain) are injected into defined areas; the detection results match the injected mask pixel-by-pixel, and CVA intensity in the loss areas is significantly higher than in stable areas, enabling offline validation.

## Dependencies / 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## Usage / 使用方法

### Basic usage

```bash
python geoskill-forest-cover-change.py --bbox 116.0 39.0 117.0 40.0 --n-dates 4
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-forest-cover-change.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2 (read multi-temporal NDVI rasters)

```bash
python geoskill-forest-cover-change.py --input ndvi_series.tif --threshold 0.3 --output-dir ./out
```

### Example 3 (stricter loss criterion)

```bash
python geoskill-forest-cover-change.py --bbox 116 39 117 40 --synthetic --drop-threshold 0.2 --output-dir ./out
```

### Example 4 (custom years + silence)

```bash
python geoskill-forest-cover-change.py --bbox 121 31 122 32 --synthetic --start-year 2001 --interval-years 3 --quiet --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `forest_change_class.tif` | GeoTIFF (int32) | 0=stable, 1=loss, 2=gain |
| `cva_magnitude.tif` | GeoTIFF (float32) | Change vector magnitude |
| `area_stats.json` | JSON | Per-class area + per-period forest area series |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- Local multi-band NDVI GeoTIFF (one period per band);
- `--synthetic` synthesizes an NDVI series offline (no network, no account required).

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; user data is never uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-forest-cover-change
description: '多期 NDVI 阈值与变化矢量幅度检测森林损失/增益/稳定，输出变化栅格与年度面积统计'
---

# 森林覆盖变化检测 | Forest Cover Change Detection

从多期 NDVI 检测森林覆盖的损失 / 增益 / 稳定。逐期用 NDVI 阈值（默认 0.3）
判定森林像元，比较首末期：由森林降为非森林且降幅 ≥ drop 阈值记为损失，
由非森林升为森林且升幅 ≥ gain 阈值记为增益，其余为稳定。同时计算
变化矢量幅度（CVA，相邻期差分的 L2 范数）量化变化强度。

典型应用：毁林监测、造林成效评估、森林资源年度变化台账。合成模式在
确定区域注入砍伐（损失）与造林（增益），检测结果与注入掩膜逐像元一致，
且损失区 CVA 强度显著高于稳定区，便于离线验证。

## 依赖

```bash
pip install 'numpy' 'rasterio' 'scipy'
```

## 使用方法

### 基本用法

```bash
python geoskill-forest-cover-change.py --bbox 116.0 39.0 117.0 40.0 --n-dates 4
```

### 示例 1（合成数据，离线）

```bash
python geoskill-forest-cover-change.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2（读取多期 NDVI 栅格）

```bash
python geoskill-forest-cover-change.py --input ndvi_series.tif --threshold 0.3 --output-dir ./out
```

### 示例 3（更严格的损失判定）

```bash
python geoskill-forest-cover-change.py --bbox 116 39 117 40 --synthetic --drop-threshold 0.2 --output-dir ./out
```

### 示例 4（自定义年份 + 静默）

```bash
python geoskill-forest-cover-change.py --bbox 121 31 122 32 --synthetic --start-year 2001 --interval-years 3 --quiet --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `forest_change_class.tif` | GeoTIFF (int32) | 0=稳定, 1=损失, 2=增益 |
| `cva_magnitude.tif` | GeoTIFF (float32) | 变化矢量幅度 |
| `area_stats.json` | JSON | 逐类面积 + 逐期森林面积序列 |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- 本地多波段 NDVI GeoTIFF（每波段一期）；
- `--synthetic` 离线合成 NDVI 序列（无需网络、无需账号）。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
