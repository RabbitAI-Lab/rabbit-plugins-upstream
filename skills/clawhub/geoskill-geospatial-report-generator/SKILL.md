---
name: geospatial-report-generator
description: >
  Render reports (HTML/DOCX/PDF) from other skills' output-manifest.json.
  Auxiliary tool only — does not analyze data, does not download anything.
  Workflow: run another skill to produce output-manifest.json first, then
  hand the manifest (or its parent directory) to this skill to render the
  final report. Use when the user already has skill outputs and wants a
  formatted deliverable document.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 不分析数据，只把 **其他 skill 的 `output-manifest.json`** 渲染成报告。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 2.4 节。

**先准备 X 文件**：先跑任意一个分析 skill 拿到 manifest。

快速试跑命令：

```bash
python geospatial_report_generator.py --input-dir ./output --format all --title 'My Report'
```


> ⚠️ **本 skill 不做数据分析，也不下载数据**。它只是「读 manifest → 渲染报告」。
> 工作流：先用其他 skill 跑出 `output-manifest.json` → 然后用本 skill 渲染成报告。
> `--bbox` / `--aoi-file` 接口仅为上下文记录 (写到 `output-manifest.json`)，不会触发任何下载。

# Geospatial Report Generator

Auxiliary report-rendering tool. Reads `output-manifest.json` (or
`qa-report.json`) from any other skill and renders it into HTML, DOCX, and/or
PDF reports. This skill does **not** analyze data, does **not** download data,
and does **not** contain any analysis or QA logic. It only formats whatever
is already present in the input manifest.

For classification purposes this skill is a **报告生成器（辅助工具）** /
**report generator (auxiliary tool)**, not an analysis skill. The
`output-manifest.json` it writes records `mode: "report_generator"` (or
`"synthetic"` when `--synthetic` is used for self-test).

## Trigger

Use when the user wants to:
- Render a report from existing skill outputs (i.e. from an
  `output-manifest.json` already produced by another skill)
- Summarize QA findings into a deliverable document (HTML/DOCX/PDF)
- Combine multiple skill outputs into one report

## Boundaries

- **Does not** perform data analysis or QA — it only formats what the
  input manifest already contains
- **Does not** download any data — fully offline, all inputs are local
  files supplied by the caller
- Conclusions are limited to what the manifest supports
- Compliance/certification requires human review

## CLI Usage

```bash
# From a single manifest
python scripts/geospatial_report_generator.py --manifest qa-output/qa-report.json

# From a directory (auto-discovers manifests)
python scripts/geospatial_report_generator.py --input-dir ./project-output

# DOCX output with custom title
python scripts/geospatial_report_generator.py --input-dir ./output --format docx --title "Flood Analysis Report"

# All formats
python scripts/geospatial_report_generator.py --manifest manifest.json --format all
```

## Arguments

| Argument | Description |
|---|---|
| `--manifest` | Path to output-manifest.json (mutual exclusive with --input-dir) |
| `--input-dir` | Directory to scan for manifests |
| `--output-dir, -o` | Output directory (default: `./report-output`) |
| `--format` | `html` (default), `docx`, `pdf`, or `all` |
| `--title` | Report title |
| `--language` | `zh` (default) or `en` |
| `--sections` | Comma-separated section names |

## Output

| File | Description |
|---|---|
| `report.html` | HTML report |
| `report.docx` | Word document (if python-docx available) |
| `report.pdf` | PDF document (if weasyprint available) |
| `report-manifest.json` | Machine-readable report metadata |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 7 | Processing failure |

## Dependencies

- Pure Python stdlib for HTML generation
- `python-docx` (optional) for DOCX output
- `weasyprint` (optional) for PDF output
- Falls back to HTML if optional deps missing
