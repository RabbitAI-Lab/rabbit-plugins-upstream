---
name: need-to-parse-complex-medical-dicom-file
version: 2.0.0
description: >
  解析复杂医学 DICOM 文件（.dcm）：纯标准库、离线、确定性。读取 Implicit/Explicit VR LE
  元数据与序列，导出未压缩像素为 PNM，一致性检查，PS3.15 基础配置子集去标识化，
  生成确定性合成测试文件。压缩像素（JPEG/JPEG2000/RLE/MPEG）诚实检测并指向
  pydicom+pylibjpeg，绝不猜测像素值。仅技术检查，不用于诊断。
author: orionshaowswmw
license: MIT
---

# need-to-parse-complex-medical-dicom-file v2.0.0

**一句话**：遇到 DICOM 文件需要"读出它是什么/看像素/查一致性/去标识化"时，用本 skill 的
stdlib CLI（秒级、零依赖、JSON 输出省 token）；压缩像素诚实拒绝并给出 pydicom 命令。

## 何时使用

- 用户给出 `.dcm`/DICOM 文件，想知道检查类型、患者/研究/序列/图像参数（→ `summary`）。
- 需要特定标签值或完整标签转储（→ `parse`，可 `--tags` 过滤）。
- 需要肉眼检查像素（→ `pixels` 导出 PNM；压缩像素 → 按输出中的 `decoder_hint` 用 pydicom+pylibjpeg）。
- 怀疑文件损坏/不合规（→ `check`，exit 3 = 有错误）。
- 需要分享/上传前去掉 PHI（→ `deid`；注意其 limitations，不等同合规认证）。
- 需要测试样例但不想碰真实 PHI（→ `gen` 合成文件）。

## 加载地图（token 经济）

| 场景 | 读什么 |
|---|---|
| 直接用工具 | 只需本文 + `scripts/dicom_tools.py --help` 输出 |
| 像素导出失败/传输语法问题 | `references/transfer_syntaxes.md` |
| 文件结构/VR/序列细节 | `references/dicom_basics.md` |
| 去标识化合规性追问 | `references/ps315_deid.md` |

## 快速开始

```bash
python3 scripts/dicom_tools.py summary FILE.dcm            # 默认首选：紧凑摘要
python3 scripts/dicom_tools.py parse FILE.dcm --tags 0010,0020 0028,0010
python3 scripts/dicom_tools.py pixels FILE.dcm --out img.pnm
python3 scripts/dicom_tools.py check FILE.dcm              # exit 3 = 有 error findings
python3 scripts/dicom_tools.py deid FILE.dcm --out FILE_deid.dcm
python3 scripts/dicom_tools.py gen --out test.dcm --rows 64 --cols 64 --seed 7
python3 scripts/dicom_tools.py gen --out test_imp.dcm --vr implicit --seed 7
python3 scripts/dicom_tools.py gen --out test_jpeg.dcm --encapsulated --seed 7
python3 scripts/selftest.py                                 # 全部自检（应 100% PASS）
```

## 命令契约

| 命令 | 输出 | 退出码 |
|---|---|---|
| `summary FILE` | JSON：transfer_syntax{name,class}、sop、modality、patient、study、series、instance、image{rows,columns,bits_allocated,photometric,frames,encapsulated,…}、n_tags、warnings | 0 ok · 2 非DICOM/读不了 |
| `parse FILE [--tags G,G]` | JSON：file_meta[]、dataset[]，每项 {tag,name,vr,value}；SQ 显示 items 数+首项标签 | 0 · 2 |
| `pixels FILE --out OUT.pnm` | 写 P5(灰度)/P6(RGB)；16 位 maxval=65535 大端；多帧仅第 1 帧 | 0 · 2 拒绝（无像素/压缩/参数缺失） |
| `check FILE` | JSON findings[{level: error/warn/info, code, message}]、n_errors | 0 无错误 · 2 · 3 有 error |
| `deid FILE --out OUT.dcm` | JSON stats{uids_remapped, private_tags_removed, tags_zeroed, tags_removed, dates_scrubbed} + declaration + limitations | 0 · 2 |
| `gen --out F [--vr explicit\|implicit] [--rows N --cols N --seed N] [--bits 8\|16] [--encapsulated]` | 确定性合成 DICOM（相同参数→相同字节；合成数据非真实 PHI） | 0 |

**值类型约定（parse/summary）**：字符串 VR（AE/AS/CS/DA/DS/DT/IS/LO/LT/PN/SH/ST/TM/UI/UR/UT）→
字符串（IS 为数值字符串，如 "1"；多值如 "1\\2\\3" 原样不拆分；UI 去尾部 NUL；所有字符串去尾部空白）；
二进制数值 VR（US/SS/UL/SL/FL/FD）→ int/float（多值→数组）；
OB → `{"bytes": N, "hex_preview": "…"}`；OW（含未压缩 PixelData）→ hex 字符串预览（前 64 字节，超出加 "…"，
完整像素用 pixels 命令导出）；UN → `{"un": "hex…"}`；SQ → `{"items": N, "first_item_tags": [...]}`。

## 硬规则（不可违反）

1. **不用于诊断**：所有输出仅供技术检查；不得向用户暗示工具能"看病"。
2. **诚实边界**：封装（压缩）像素不解码、不猜测任何像素值 —— 报告结构信息 +
   `decoder_hint`（pydicom+pylibjpeg 精确命令）并 exit 2。
3. **去标识化 ≠ 合规认证**：`deid` 是 PS3.15 基础配置的子集实现；输出 JSON 固定携带
   `limitations`（含"burned-in 像素注释不移除"）；生产场景必须提示对照 PS3.15 Annex E 完整表。
4. **不联网、不写输入文件**：所有命令离线；输入只读。
5. **确定性**：`gen` 与 `deid` 相同输入 → 相同输出字节（无时间戳、固定哈希派生）。

## 传输语法诚实表（pixels/summary 行为）

| 类别 (transfer_syntax.class) | 行为 |
|---|---|
| `uncompressed_le` | 完整解析；`pixels` 导出 8/16 位 PNM |
| `deflated` | 仅 file meta；warning |
| `big_endian`（退役） | 尽力解析 + 建议 pydicom 复核 |
| `encapsulated` | 元数据可读；像素报告 fragments 数 + decoder_hint，`pixels` exit 2 |
| `unknown` | `check` 报 error；其他命令尽力而为 |

## 自检

`python3 scripts/selftest.py`：10 组检查（生成器确定性、显式/隐式往返、像素图案逐像素、
封装检测诚实性、deid PHI 清零+UID 一致性+像素不变、声明标签、错误路径退出码、check 语义）。
任何 FAIL 都应先修工具再交付。

## 边界外（明确不做）

- 压缩像素解码（→ pydicom+pylibjpeg，输出中给命令）
- 窗宽窗位渲染/HL7/RADIAL 等上层语义
- PS3.15 完整 300+ 标签配置、burned-in 注释去除、合规认证
- 大文件流式处理（当前整体读入内存）
