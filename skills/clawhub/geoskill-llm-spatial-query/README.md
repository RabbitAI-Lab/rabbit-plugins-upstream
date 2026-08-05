# LLM Spatial Query (geoskill-llm-spatial-query)

> Natural-language rule parsing + geopandas spatial query, outputting query-result GeoJSON (offline numpy-equivalent implementation)

---

## 1. Overview

Perform attribute + spatial queries on a vector layer with a single natural-language sentence (e.g., "select parcels with area > 50 and take the top 3 by value"), outputting the matched features as GeoJSON along with a structured query plan. This skill is an **offline numpy-equivalent implementation** of an LLM/NL2GeoSQL spatial question-answering system: it does not depend on a large model, parsing the text into a query plan (fields/operators/values, bbox spatial intent, sorting and Top-N) with regex rules, then executing it with geopandas/shapely; the query plan is persisted as JSON and is fully auditable and unit-testable.

## 2. Features

Perform attribute + spatial queries on a vector layer with a single natural-language sentence (e.g., "select parcels with area > 50 and take the top 3 by value"), outputting the matched features as GeoJSON along with a structured query plan. This skill is an **offline numpy-equivalent implementation** of an LLM/NL2GeoSQL spatial question-answering system: it does not depend on a large model, parsing the text into a query plan (fields/operators/values, bbox spatial intent, sorting and Top-N) with regex rules, then executing it with geopandas/shapely; the query plan is persisted as JSON and is fully auditable and unit-testable.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-llm-spatial-query.py --bbox 116 39 117 40 --synthetic --output-dir ./out
```

## 4. CLI Parameters

Run `python <skill>.py --help` for the full list. Common parameters:

| Parameter | Type | Description |
|---|---|---|
| `--bbox` | `float[4]` | WGS84 bounding box `min_lon min_lat max_lon max_lat` |
| `--input` | `path` | Local input file (GeoJSON/GeoTIFF/etc.) |
| `--output-dir` | `path` | Output directory (default `./output`) |
| `--synthetic` | `flag` | Use synthetic data instead of real input |
| `--quiet` | `flag` | Suppress non-essential stdout |

## 5. Input / Output

| File | Format | Description |
|---|---|---|
| `query_result.geojson` | GeoJSON | Matched feature set |
| `query_plan.json` | JSON | Parsed structured query plan |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |


## 6. Technical Principle

(see SKILL.md for details)

## 7. Methodology

This skill has been methodologically reviewed. See [`REVIEW.md`](./REVIEW.md) for:

- P0/P1/P2 issue counts and verdicts
- Reproduction commands
- Known limitations and edge cases

## 8. License

MIT License. See [`LICENSE`](./LICENSE) for full text.

---

# LLM空间查询（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

---
name: geoskill-llm-spatial-query
description: '自然语言规则解析+geopandas空间查询，输出查询结果GeoJSON（离线numpy等价实现）'
---

# LLM空间查询 | LLM Spatial Query

用一句自然语言（如"筛选面积大于 50 的地块，取值最高的前 3 个"）对矢量图层做属性 + 空间查询，输出命中要素 GeoJSON 与结构化查询计划。

本 skill 是 LLM/NL2GeoSQL 空间问答系统的**离线 numpy 等价实现**：不依赖大模型，用正则规则把文本解析成查询计划（字段/比较符/数值、bbox 空间意图、排序与 Top-N），再用 geopandas/shapely 执行；查询计划落盘为 JSON，完全可审计、可单测。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-llm-spatial-query.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成地块查询（离线）

```bash
python geoskill-llm-spatial-query.py --bbox 116.0 39.0 117.0 40.0 --synthetic --query "面积大于50的前3个" --output-dir ./out
```

### 示例 3：真实矢量属性查询

```bash
python geoskill-llm-spatial-query.py --input parcels.geojson --query "人口小于3000" --output-dir ./out
```

### 示例 4：空间范围查询

```bash
python geoskill-llm-spatial-query.py --bbox 116.0 39.0 116.5 39.5 --synthetic --query "在范围内的地块" --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `query_result.geojson` | GeoJSON | 命中要素集合 |
| `query_plan.json` | JSON | 解析出的结构化查询计划 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

本地矢量文件（GeoJSON/Shapefile），或 --synthetic 规则地块网格图层。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
