---
name: geoskill-ai-report-generator
description: '分析结果JSON模板填充，生成结构化HTML/Markdown报告（离线numpy等价实现）'
---

# AI遥感分析报告生成 | AI Remote Sensing Report Generator

Automatically renders remote sensing analysis results (metric dictionaries / per-band raster statistics / JSON files) into structured reports: title, metadata, overview statistics, metric detail tables, threshold ratings (PASS/WARN/FAIL) and conclusions, supporting both HTML and Markdown formats.

This skill is an **offline NumPy-equivalent implementation** of an LLM-driven automatic reporting system: it reproduces the report generation pipeline without relying on a large model, using "result parsing -> summary statistics and threshold rating (rule-based conclusion generation) -> HTML-escaped template filling"; all dynamic content is HTML-escaped to prevent injection.

## Dependencies / 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## Usage / 使用方法

### Example 1 (Synthetic Data, Offline)

```bash
python geoskill-ai-report-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: Synthetic Sample Report (Offline)

```bash
python geoskill-ai-report-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --title "parcel monthly report" --output-dir ./out
```

### 示例 3：分析结果 JSON -> 报告

```bash
python geoskill-ai-report-generator.py --analysis results.json --title "monitoring report" --format both --output-dir ./out
```

### Example 4: Automatic Raster Statistics to Report

```bash
python geoskill-ai-report-generator.py --input scene.tif --format md --output-dir ./out
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `report.html` | HTML | Standalone HTML report with inline styles |
| `report.md` | Markdown | Markdown report with the same content |
| `report_summary.json` | JSON | Summary statistics + rating flags + raw results |
| `output-manifest.json` | JSON | Run manifest (inputs/outputs/QA/exit code) |

## Data Source / 数据源 / Source

Analysis result JSON / local GeoTIFF (per-band statistics computed automatically), or --synthetic example results.

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is done locally; no user data is ever uploaded.

## License / License

MIT

---


<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-ai-report-generator
description: '分析结果JSON模板填充，生成结构化HTML/Markdown报告（离线numpy等价实现）'
---

# AI遥感分析报告生成 | AI Remote Sensing Report Generator

把遥感分析结果（指标字典 / 栅格逐波段统计 / JSON 文件）自动渲染成结构化报告：含标题、元信息、概览统计、指标明细表、阈值评级（PASS/WARN/FAIL）与结论，支持 HTML 与 Markdown 双格式。

本 skill 是 LLM 自动报告系统的**离线 numpy 等价实现**：不依赖大模型，用"结果解析 -> 摘要统计与阈值评级（规则化结论生成）-> HTML 转义安全的模板填充"复现报告生成流程；所有动态内容经 HTML 转义，杜绝注入。

## 依赖

```bash
pip install numpy rasterio scipy scikit-learn geopandas shapely
```

## 使用方法

### 示例 1（合成数据，离线）

```bash
python geoskill-ai-report-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：合成示例报告（离线）

```bash
python geoskill-ai-report-generator.py --bbox 116.0 39.0 117.0 40.0 --synthetic --title "地块月报" --output-dir ./out
```

### 示例 3：分析结果 JSON -> 报告

```bash
python geoskill-ai-report-generator.py --analysis results.json --title "监测报告" --format both --output-dir ./out
```

### 示例 4：栅格自动统计成报告

```bash
python geoskill-ai-report-generator.py --input scene.tif --format md --output-dir ./out
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `report.html` | HTML | 带内联样式的独立 HTML 报告 |
| `report.md` | Markdown | 同内容 Markdown 报告 |
| `report_summary.json` | JSON | 摘要统计 + 评级旗标 + 原始结果 |
| `output-manifest.json` | JSON | 运行清单（输入/输出/QA/退出码） |

## 数据源 / Source

分析结果 JSON / 本地 GeoTIFF（自动算逐波段统计），或 --synthetic 示例结果。

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传任何用户数据。

## License

MIT
