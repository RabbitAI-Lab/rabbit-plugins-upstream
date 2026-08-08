# AI Remote Sensing Analysis Report Generation (geoskill-ai-report-generator)

> Fills analysis-result JSON into templates to generate structured HTML/Markdown reports (offline numpy equivalent implementation)

---

## 1. Overview

Automatically renders remote sensing analysis results (metric dictionaries / per-band raster statistics / JSON files) into structured reports: title, metadata, overview statistics, metric detail tables, threshold ratings (PASS/WARN/FAIL) and conclusions, supporting both HTML and Markdown formats. This skill is an **offline numpy equivalent implementation** of an LLM-based automatic report system: without relying on a large model, it reproduces the report generation pipeline with "result parsing → summary statistics and threshold rating (rule-based conclusion generation) → HTML-escape-safe template filling"; all dynamic content is HTML-escaped to prevent injection.

## 2. Features

Automatically renders remote sensing analysis results (metric dictionaries / per-band raster statistics / JSON files) into structured reports: title, metadata, overview statistics, metric detail tables, threshold ratings (PASS/WARN/FAIL) and conclusions, supporting both HTML and Markdown formats. This skill is an **offline numpy equivalent implementation** of an LLM-based automatic report system: without relying on a large model, it reproduces the report generation pipeline with "result parsing → summary statistics and threshold rating (rule-based conclusion generation) → HTML-escape-safe template filling"; all dynamic content is HTML-escaped to prevent injection.

## 3. Quick Start

```bash
pip install -r requirements.txt
python geoskill-ai-report-generator.py --bbox 116 39 117 40 --synthetic --output-dir ./out
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
| `report.html` | HTML | Self-contained HTML report with inline styles |
| `report.md` | Markdown | Markdown report with the same content |
| `report_summary.json` | JSON | Summary statistics + rating flags + raw results |
| `output-manifest.json` | JSON | Run manifest (input/output/QA/exit code) |


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

# AI遥感分析报告生成（中文版）

> 本部分为完整中文文档，与上方英文部分对应。

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
