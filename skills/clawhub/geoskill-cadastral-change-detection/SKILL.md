---
name: cadastral-change-detection
description: >
  Topology-aware cadastral parcel change detection between two epochs.
  Identifies new, deleted, expanded, reduced, split, and merged parcels
  from cadastral vector data (宗地/地块/调查图斑). Use when comparing
  two epochs of land parcels, auditing boundary changes, or generating
  cadastral change ledgers.
---

## Prerequisites / 先准备 X 文件

> ⚠️ **必读** — 本 skill 不属于即用型，需要先准备特定文件才能跑。

本 skill 需要 **两期宗地矢量**（GeoJSON / Shapefile），来自地方不动产登记。

👉 完整教程见仓库根目录 `PREREQUISITES.md` 2.1 节。

**先准备 X 文件**：`references/sample_before.geojson` + `references/sample_after.geojson` 试跑，再换成真实宗地。

快速试跑命令：

```bash
python cadastral_change_detection.py --before references/sample_before.geojson --after references/sample_after.geojson --output-dir ./test
```


# Cadastral Change Detection

Compares two epochs of cadastral parcels to detect object-level changes with topology awareness.

## Trigger

Use when the user wants to:
- Compare two epochs of parcel/cadastral data
- Identify new/deleted/changed parcels
- Detect split and merge events
- Audit boundary adjustments
- Generate change ledgers and topology issue reports

## CLI Usage

```bash
# Basic comparison
python scripts/cadastral_change_detection.py \
  --before before.geojson \
  --after after.geojson

# With custom parameters
python scripts/cadastral_change_detection.py \
  --before before.geojson \
  --after after.geojson \
  --id-field ZDBM \
  --field-map field_map.json \
  --tolerance 0.3 \
  --area-threshold 0.1 \
  --match-iou 0.1 \
  --output-dir ./ccd-output

# Dry run (validate only)
python scripts/cadastral_change_detection.py \
  --before before.geojson \
  --after after.geojson \
  --dry-run
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--before` | required | 前期宗地数据 (GeoJSON/Shapefile) |
| `--after` | required | 后期宗地数据 (GeoJSON/Shapefile) |
| `--id-field` | auto | 宗地唯一标识字段名 |
| `--field-map` | None | 字段映射 JSON (前期字段→后期字段) |
| `--tolerance` | 0.0 | 几何容差 (CRS 单位) |
| `--area-threshold` | 0.05 | 面积变化阈值比例 |
| `--match-iou` | 0.1 | IoU 匹配阈值 |
| `--rules` | None | 业务规则 JSON 文件路径 |
| `--output-dir` | ./cadastral-change-output | 输出目录 |
| `--dry-run` | False | 仅验证参数 |
| `--bbox` | None | (reserved) standard flag, has no effect on this skill |
| `--date-range` | None | (reserved) standard flag, has no effect on this skill |
| `--aoi-file` | None | (reserved) standard flag, has no effect on this skill |

## 数据下载 (Data Download)

This skill does **not** auto-download cadastral data. Cadastral /
land-parcel datasets are jurisdiction-specific and not available from
open archives. The user must supply two epochs of vector data
(`--before` and `--after`).

The `--bbox`, `--date-range`, and `--aoi-file` flags are still
registered (for CLI consistency with the other 49 GeoSkills) but
have no effect on the analysis. Supplying `--bbox` without
`--before/--after` raises a clear error.

## Output

| File | Description |
|---|---|
| `parcel_changes.geojson` | 变更宗地图层（含变更类型与指标） |
| `change_ledger.xlsx` | 变更台账（Excel 汇总表） |
| `topology_issues.geojson` | 拓扑问题图层（重叠/缝隙） |
| `field_changes.csv` | 属性字段变更记录 |
| `audit_report.pdf` | 审核报告（HTML 格式） |
| `request.json` | 请求参数记录 |
| `dataset-manifest.json` | 数据集清单 |
| `output-manifest.json` | 输出清单 |
| `qa.json` | 质量检查结果 |
| `run.log` | 运行日志 |

## Change Types

| Type | Meaning |
|---|---|
| `new` | 新增宗地（仅后期存在） |
| `deleted` | 删除宗地（仅前期存在） |
| `expanded` | 面积扩大（超阈值） |
| `reduced` | 面积缩小（超阈值） |
| `unchanged` | 未变化（面积在容差内） |
| `split` | 分割（1前期→N后期） |
| `merge` | 合并（N前期→1后期） |
| `boundary_adjust` | 边界调整（面积不变但边界位移） |

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 依赖缺失 |
| 6 | 数据校验失败 |
| 7 | 处理失败 |

## Constraints

- 几何容差按 CRS 单位配置，禁止在经纬度直接用米容差
- 图匹配处理一对多/多对一并保存映射
- 面积差区分几何精度误差与业务阈值
- 敏感数据默认不联网、不上传
