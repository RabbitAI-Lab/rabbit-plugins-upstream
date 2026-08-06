---
name: geoskill-hyperspectral-unmixing
description: 'VCA/N-FINDR端元提取+nnls线性解混丰度反演'
---

# 高光谱端元提取与解混 | Hyperspectral Endmember Extraction & Unmixing

Extracts pure endmember spectra from hyperspectral imagery and inverts per-pixel abundances. Two classic endmember-extraction algorithms are supported:

- **VCA** (Vertex Component Analysis): iteratively seeks the projection direction with maximum variance in PCA-projected space and takes the extreme pixels as endmembers;
- **N-FINDR** (simplified): a greedy iterative search for the pixel combination that maximizes the simplex volume.

Linear unmixing uses FCLSU: for each pixel, `scipy.optimize.nnls` solves for non-negative least-squares abundances, which are then normalized to sum to 1 (abundance sum-to-one constraint); a residual map is also output to evaluate fit quality. Suitable for mixed-pixel decomposition, mineral/vegetation abundance mapping, and sub-pixel analysis.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy
```

## Usage / 使用方法

### Basic Usage (Synthetic Data, Offline)

```bash
python geoskill-hyperspectral-unmixing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1: VCA with 3 Endmembers

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-endmembers 3 --method vca \
    --output-dir ./vca_3em
```

### Example 2: N-FINDR Method Comparison

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --n-endmembers 4 --method nfindr \
    --output-dir ./nfindr_4em
```

### Example 3: More Bands

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 40 --n-endmembers 3 \
    --output-dir ./vca_40bands
```

### Example 4: Real Hyperspectral GeoTIFF Input

```bash
python geoskill-hyperspectral-unmixing.py \
    --input cuprite_subset.tif --n-endmembers 5 --method vca \
    --output-dir ./real_vca
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `abundances.tif` | GeoTIFF (float32, one band per endmember) | Normalized abundance map [0,1], EPSG:4326 |
| `residual.tif` | GeoTIFF (float32) | Linear unmixing residual (RMSE) map |
| `endmembers.json` | JSON | Endmember spectra, algorithm, matching diagnostics |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/software versions) |

## Data Source / 数据源 / Source

- **Real mode**: local hyperspectral GeoTIFF
- **Synthetic mode**: defines endmember spectra locally and generates pixels by linear mixing with random abundances plus noise; no external data source

## Privacy / 隐私声明 / Privacy

- Runs fully offline by default and makes no network requests
- `--synthetic` mode reads no external data
- All computation is done locally; user data is never uploaded

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-hyperspectral-unmixing
description: 'VCA/N-FINDR端元提取+nnls线性解混丰度反演'
---

# 高光谱端元提取与解混 | Hyperspectral Endmember Extraction & Unmixing

从高光谱影像中提取纯净端元（endmember）光谱并反演逐像元丰度
（abundance）。端元提取支持两种经典算法：

- **VCA**（Vertex Component Analysis）：在 PCA 投影空间中迭代寻找
  方差最大的投影方向，取极值像元作为端元；
- **N-FINDR**（简化版）：贪心迭代搜索使单纯体体积最大的像元组合。

线性解混采用 FCLSU：对每个像元用 `scipy.optimize.nnls` 求非负最小
二乘丰度，再归一化到和为 1（丰度总和约束），并输出残差图评估拟合
质量。适用于混合像元分解、矿物/植被丰度制图、亚像元分析。

## 依赖

```bash
pip install numpy rasterio scipy
```

## 使用方法

### 基本用法（合成数据，离线）

```bash
python geoskill-hyperspectral-unmixing.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1：VCA 提取 3 个端元

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-endmembers 3 --method vca \
    --output-dir ./vca_3em
```

### 示例 2：N-FINDR 方法对比

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 121.0 31.0 122.0 32.0 \
    --synthetic --n-endmembers 4 --method nfindr \
    --output-dir ./nfindr_4em
```

### 示例 3：更多波段

```bash
python geoskill-hyperspectral-unmixing.py \
    --bbox 116.0 39.0 117.0 40.0 \
    --synthetic --n-bands 40 --n-endmembers 3 \
    --output-dir ./vca_40bands
```

### 示例 4：真实高光谱 GeoTIFF 输入

```bash
python geoskill-hyperspectral-unmixing.py \
    --input cuprite_subset.tif --n-endmembers 5 --method vca \
    --output-dir ./real_vca
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `abundances.tif` | GeoTIFF (float32, 每端元一波段) | 归一化丰度图 [0,1]，EPSG:4326 |
| `residual.tif` | GeoTIFF (float32) | 线性解混残差（RMSE）图 |
| `endmembers.json` | JSON | 端元光谱、算法、匹配诊断 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/软件版本） |

## 数据源 / Source

- **真实模式**：本地高光谱 GeoTIFF
- **合成模式**：本地定义端元光谱，按随机丰度线性混合 + 噪声生成像元，
  无外部数据源

## 隐私声明 / Privacy

- 默认完全离线运行，不发起任何网络请求
- `--synthetic` 模式不读取任何外部数据
- 所有计算在本地完成，不上传用户数据

## License

MIT
