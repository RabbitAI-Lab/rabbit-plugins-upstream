---
name: geoskill-metadata-standards-checker
description: '解析 ISO 19115 / FGDC 格式 XML 元数据，验证必填项、受控词表与一致性规则，输出完整性评分与问题清单。Parse ISO 19115 / FGDC XML metadata, validate required fields and controlled vocabularies, and report a completeness score.'
---

# 元数据标准检查 | Metadata Standards Checker

Performs standards-compliance checks on the XML metadata of geospatial data. Two major standards are supported: **ISO 19115** (gmd:MD_Metadata framework) and **FGDC** (the U.S. Federal Geographic Data Committee CSDGM framework). The checker parses the XML, extracts elements in a namespace-agnostic way, and then validates each item against the required-field lists and controlled vocabularies of the respective standard (e.g., hierarchyLevel, topicCategory).

Core algorithm: namespace-stripped element extraction → automatic standard detection (ISO / FGDC) → required-field hit counting yields a 0-1 completeness score → two-level error/warning issue list → controlled-vocabulary compliance check. Suitable for metadata QA before data submission and validation before ingest into catalog systems.

A built-in `--synthetic` mode generates complete and deliberately deficient ISO/FGDC sample metadata locally, so the full checking workflow can be demonstrated without real data.

## Dependencies / 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## Usage / 使用方法

### Basic Usage

```bash
python geoskill-metadata-standards-checker.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 1 (synthetic data, offline)

```bash
python geoskill-metadata-standards-checker.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### Example 2: check a single ISO 19115 file

```bash
python geoskill-metadata-standards-checker.py --input dataset_iso.xml --standard iso19115 --output-dir ./report
```

### Example 3: check FGDC metadata

```bash
python geoskill-metadata-standards-checker.py --input fgdc_meta.xml --standard fgdc --output-dir ./report_fgdc
```

### Example 4: auto-detect the standard

```bash
python geoskill-metadata-standards-checker.py --input unknown.xml --standard auto --output-dir ./auto
```

### Example 5: silent batch processing (for use with shell loops)

```bash
python geoskill-metadata-standards-checker.py --input one.xml --quiet --output-dir ./r1
python geoskill-metadata-standards-checker.py --input two.xml --quiet --output-dir ./r2
```

## Output / 输出

| File | Format | Description |
|---|---|---|
| `metadata_report.json` | JSON | Per-file scores, error/warning issue list, overall statistics |
| `samples/*.xml` | XML | Sample metadata generated in synthetic mode (synthetic mode only) |
| `output-manifest.json` | JSON | Run manifest |

## Data Source / 数据源 / Source

- `--input`: local XML metadata file
- `--synthetic`: locally generated ISO 19115 / FGDC samples, no external data source

## Privacy / 隐私声明 / Privacy

- Runs offline by default; `--synthetic` mode requires no network at all.
- All processing is performed locally; no user data is uploaded.

## License / License

MIT

---

<!-- ===== 中文原文 (Chinese Original) ===== -->

---
name: geoskill-metadata-standards-checker
description: '解析 ISO 19115 / FGDC 格式 XML 元数据，验证必填项、受控词表与一致性规则，输出完整性评分与问题清单。Parse ISO 19115 / FGDC XML metadata, validate required fields and controlled vocabularies, and report a completeness score.'
---

# 元数据标准检查 | Metadata Standards Checker

对地理数据的 XML 元数据执行标准符合性检查。支持两大主流标准：
**ISO 19115**（gmd:MD_Metadata 体系）与 **FGDC**（美国联邦地理数据委员会
CSDGM 体系）。检查器解析 XML、按命名空间无关的方式提取元素，然后对照各
标准的必填项清单与受控词表（如 hierarchyLevel、topicCategory）逐条验证。

核心算法：命名空间剥离的元素提取 → 标准自动判定（ISO / FGDC）→ 必填项
命中计数得到 0-1 完整性评分 → error/warning 两级问题清单 → 受控词表
合规检查。适合数据汇交前的元数据质检、目录系统入库校验。

内置 `--synthetic` 模式，会在本地生成完整版与刻意缺漏版的 ISO/FGDC 样例
元数据，无需真实数据即可完整演示检查流程。

## 依赖

```bash
pip install numpy rasterio geopandas shapely fiona pyproj
```

## 使用方法

### 基本用法

```bash
python geoskill-metadata-standards-checker.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 1（合成数据，离线）

```bash
python geoskill-metadata-standards-checker.py --bbox 116.0 39.0 117.0 40.0 --synthetic --output-dir ./out
```

### 示例 2：检查单个 ISO 19115 文件

```bash
python geoskill-metadata-standards-checker.py --input dataset_iso.xml --standard iso19115 --output-dir ./report
```

### 示例 3：检查 FGDC 元数据

```bash
python geoskill-metadata-standards-checker.py --input fgdc_meta.xml --standard fgdc --output-dir ./report_fgdc
```

### 示例 4：自动判定标准

```bash
python geoskill-metadata-standards-checker.py --input unknown.xml --standard auto --output-dir ./auto
```

### 示例 5：静默批处理（配合 shell 循环）

```bash
python geoskill-metadata-standards-checker.py --input one.xml --quiet --output-dir ./r1
python geoskill-metadata-standards-checker.py --input two.xml --quiet --output-dir ./r2
```

## 输出

| 文件 | 格式 | 说明 |
|---|---|---|
| `metadata_report.json` | JSON | 逐文件评分、error/warning 问题清单、总体统计 |
| `samples/*.xml` | XML | 合成模式生成的样例元数据（仅 synthetic 模式） |
| `output-manifest.json` | JSON | 运行清单 |

## 数据源 / Source

- `--input`：本地 XML 元数据文件
- `--synthetic`：本地生成的 ISO 19115 / FGDC 样例，无外部数据源

## 隐私声明 / Privacy

- 默认离线运行，`--synthetic` 模式完全无网络。
- 所有处理在本地完成，不上传用户数据。

## License

MIT
