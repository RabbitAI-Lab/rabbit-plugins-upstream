# DICOM 文件结构速查（供参考 · 定性）

> 依据：DICOM PS3.5 2026c（NEMA, DICOM Standard Part 5: Data Structures and Encoding），
> 2026-09-06 核对 https://dicom.nema.org/medical/dicom/current/output/html/part05.html
> 用途：本 skill 解析器的设计依据；**定性参考，非诊断/合规依据**。

## 1. 文件总体布局（PS3.5 §8 / A.4）

```
偏移        内容
0..127      Preamble（128 字节，通常全 0；可含任意值）
128..131    Magic: ASCII "DICM"（无 NUL）
132..       File Meta Information（组 0002，总是 Explicit VR Little Endian）
...         Dataset（编码方式由 (0002,0003) TransferSyntaxUID 决定）
```

- 缺 "DICM" 魔数 → 不是标准 DICOM Part10 文件（可能为裸数据集，本工具不处理）。
- File Meta 必须元素：
  - (0002,0001) MediaStorageSOPClassUID (UI)
  - (0002,0002) MediaStorageSOPInstanceUID (UI)
  - (0002,0003) TransferSyntaxUID (UI)

## 2. 数据元素结构（PS3.5 §7.1.2 / §7.1.3）

### Explicit VR（Little/Big Endian）
```
Group (2B)  Element (2B)  VR (2B ASCII)
  - 普通 VR:  Reserved (2B) + Value Length (2B)
  - OB/OW/SQ/UC/UR/UT: Reserved (4B) + Value Length (4B)
Value (Length bytes)
```
Length = 0xFFFFFFFF → 未定义长度（仅 SQ 与封装像素数据合法）。

### Implicit VR（Little Endian）
```
Group (2B)  Element (2B)  Value Length (2B)
Value (Length bytes)   ← VR 不存于文件中，由数据字典推断
```
- 本工具用内置常见标签 VR 表（约 50 项）推断；未列出者按 UN 处理并给出十六进制预览（诚实降级）。

### 序列（PS3.5 §7.5）
- SQ 元素，未定义长度时内容为一串 Item：
  - Item: FFFE,E000 + Length(2B)（可 0xFFFFFFFF 未定义）
  - Item Delimitation: FFFE,E00D + 0000
  - Sequence Delimitation: FFFE,E0DD + 0000（终止 SQ）
- **继承规则（§7.5.3）**：序列内部元素总按 Explicit VR 解析，与外层传输语法无关。
- 注意区分：封装像素数据内的 FFFE,E000 项长度字段为 **4 字节**（PS3.5 §8.2），SQ 内 Item 为 2 字节。

### 私有标签（PS3.5 §7.8）
- Group 号为奇数 → 私有创建者/私有数据元素；VR 无字典约束，隐式文件中 VR 不可知。
- 去标识化时**必须整体移除**（最常见 PHI 泄漏源）。

### 组长度（PS3.5 §7.2）
- (GGGG,0000) 记录本组字节长度；可存在也可不存在，读取器不应依赖。

## 3. 值表示要点（PS3.5 §6.2 / §A.4.2）

| 类别 | VR 例 | 编码 |
|---|---|---|
| 字符串 | AE AS CS DA DS DT IS LO LT PN SH ST TM UI UR UT | ASCII/Latin-1；IS 为数值字符串；UI 可 NUL 结尾；奇数字节值补 1 空格 |
| 数值（小端） | US SS UL SL FL FD | 2/4/8 字节，按传输语法端序 |
| 二进制 | OB OW UN | 原始字节；UN = 创建者私有，语义不可知 |

- 未压缩像素 (7FE0,0010) 通常 VR=OW（小端逐样本）；16 位 PNM 导出需转大端（PNM 规范）。
- 多帧：NumberOfFrames (0028,0008)，帧按行主序连续存放。

## 4. 本工具支持的边界（诚实声明）

| 能力 | 状态 |
|---|---|
| Implicit VR LE (1.2.840.10008.1.2) 解析 | ✓ |
| Explicit VR LE (1.2.840.10008.1.2.1) 解析 | ✓ |
| 序列（含嵌套 ≤8 层）、私有标签 | ✓ |
| 未压缩 8/16 位像素 → PNM | ✓ |
| JPEG/JPEG-LS/JPEG2000/RLE/MPEG 解码 | ✗（检测+报告+指向 pydicom/pylibjpeg，绝不猜测像素） |
| Deflated Explicit VR LE | ✗（仅 file meta，报告警告） |
| Explicit VR Big Endian（已退役） | △（尽力解析，提示用 pydicom 复核） |
| 诊断用途 | ✗（仅技术检查） |

## 5. 关键标签名表（本工具内置，常用子集）

PatientName (0010,0010) PN · PatientID (0010,0020) LO · PatientBirthDate (0010,0030) DA ·
PatientSex (0010,0040) CS · SOPClassUID (0008,0016) UI · SOPInstanceUID (0008,0018) UI ·
Modality (0008,0060) CS · StudyDate (0008,0020) DA · AccessionNumber (0008,0050) SH ·
StationName (0008,0070) SH · InstitutionName (0008,0080) LO · ReferringPhysicianName (0008,0090) PN ·
StudyInstanceUID (0020,000D) UI · SeriesInstanceUID (0020,000E) UI · SeriesNumber (0020,0011) IS ·
InstanceNumber (0020,0013) IS · Rows (0028,0010) US · Columns (0028,0011) US ·
SamplesPerPixel (0028,0002) US · PhotometricInterpretation (0028,0004) CS ·
BitsAllocated (0028,0100) US · BitsStored (0028,0101) US · HighBit (0028,0102) US ·
PixelRepresentation (0028,0103) US · PixelData (7FE0,0010) OW/OB ·
PatientIdentityRemoved (0012,0062) CS · DeidentificationMethodCodeSequence (0012,0063) SQ

（完整字典见 PS3.6 Data Dictionary；本表为常用子集，未列标签以 [GGGG,EEEE] 显示。）
