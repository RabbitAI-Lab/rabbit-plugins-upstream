# 去标识化（De-identification）设计依据（供参考 · 定性）

> 依据：DICOM PS3.15 2026c（NEMA, Part 15: Security and System Management Profiles）
> §6.9 Attribute Confidentiality Profiles / Annex E "Basic Application Level
> Confidentiality Profile"（2026-09-06 核对 https://dicom.nema.org/medical/dicom/current/output/html/part15.html ），
> 及多来源实践（micheledpierri 2026-07-19 · healthcareonlinetools 2026-03-17 · fast.io 2026-04-22）。
> **供参考：生产使用前必须对照 PS3.15 2026c Annex E 权威 300+ 标签表核实。**

## 1. PS3.15 动作码（Annex E 定义）

| 码 | 含义 | 本工具实现 |
|---|---|---|
| K | Keep 保留 | PatientSex、PatientWeight/Height、诊断相关标签 |
| D | Dummy 哑值 | （本工具子集中用 Z 替代：置空字符串，语义等效且更保守） |
| Z | Zero-length 置零长（保留标签，值为空） | 直接标识符（PatientName/PatientID/…） |
| X | Delete 移除 | 可安全移除的标识符（OtherPatientIDs/Names、Address、Phone、InstitutionAddress） |
| C | Clean 清洗 | — |
| U | UID remap 重映射 | 全部 UID 确定性哈希重映射 |

要点（PS3.15 + 实践共识）：
1. **Type 1 必需标签只能置空/哑值，不能移除**（PatientName/PatientID 等移除会导致文件不合规）。
2. **私有标签（奇数组）= 最常见泄漏源 → 全部移除**。
3. **日期按 VR（DA/DT/TM）批量清洗**，不能只靠标签名（自定义日期标签名不在已知表里）。
4. **UID 必须一致性重映射**（同一 UID → 同一新 UID，跨文件/跨批次一致），
   保持 Study/Series/Instance 层级关联，同时与源系统不可链接。
5. **合规声明**：写入 PatientIdentityRemoved (0012,0062) = "YES"
   + DeidentificationMethodCodeSequence (0012,0063)（SQ，含 CodeValue/CodingSchemeDesignator 的 item）。

## 2. 本工具实现的直接标识符子集（deid 命令）

| 标签 | 名称 | 动作 |
|---|---|---|
| (0010,0010) | PatientName | Z 置空 |
| (0010,0020) | PatientID | Z 置空 |
| (0010,0030) | PatientBirthDate | Z 置空 |
| (0010,0032) | PatientAge | Z 置空 |
| (0010,1000) | OtherPatientIDs | X 移除 |
| (0010,1001) | OtherPatientNames | X 移除 |
| (0010,1040) | PatientAddress | X 移除 |
| (0010,2154) | PatientTelephoneNumbers | X 移除 |
| (0008,0050) | AccessionNumber | Z 置空 |
| (0008,0070) | StationName | Z 置空 |
| (0008,0080) | InstitutionName | Z 置空 |
| (0008,0081) | InstitutionAddress | X 移除 |
| (0008,0090) | ReferringPhysicianName | Z 置空 |
| (0008,0092) | ReferringPhysicianAddress | Z 置空 |
| (0008,1040) | InstitutionalDepartmentName | Z 置空 |
| (0008,1048) | PhysiciansOfRecord | Z 置空 |
| (0008,1050) | PerformingPhysicianName | Z 置空 |
| (0008,1070) | OperatorsName | Z 置空 |
| (0008,1110) | ReferringPhysicianIdentificationSequence | Z 空序列 |
| (0020,0010) | StudyID | Z 置空 |
| 全部 DA/DT/TM | 任意日期/时间 | 置 1900-01-01 / 00:00:00.000000 |
| 全部奇数组标签 | 私有标签 | X 移除 |
| UID 类（见下） | 全部 UID | U 重映射 |

UID 重映射范围：MediaStorageSOPInstanceUID (0002,0002) · SOPInstanceUID (0008,0018) ·
StudyInstanceUID (0020,000D) · SeriesInstanceUID (0020,000E) · FrameOfReferenceUID (0020,0052) ·
OtherStudyUID (0020,0070) · RTPlanLabel 相关 (0040,0551)。

**重映射算法（确定性、不可逆、批次内一致）：**
```
new_uid = "1.2.826.0.1.3680043.8.498." + sha256(old_uid).hexdigest()[:16]
```
- 同一 old_uid 永远 → 同一 new_uid（跨文件、跨运行一致）。
- 不保存、不输出 old→new 映射表（避免重识别风险）。

**合规声明写入：**
- (0012,0062) PatientIdentityRemoved = "YES" (CS)
- (0012,0063) DeidentificationMethodCodeSequence = SQ，单 item：
  - (0008,0070) CodeValue = "113040" (SH)
  - (0008,0080) CodingSchemeDesignator = "DCM" (SH)
  - (0008,0102) CodeMeaning = "De-identification using Basic Application Level Confidentiality Profile" (LO)
- 重复 deid 时先移除旧声明再写入新声明（避免重复元素）。

## 3. 诚实局限（deid 输出 JSON 中固定附带 limitations 字段）

1. 本工具实现 PS3.15 基础配置的**直接标识符子集（约 20 标签 + 按 VR 日期清洗 + 私有标签移除）**；
   权威完整表为 PS3.15 2026c Annex E（300+ 标签，含设备、地点、日期偏移策略等），
   生产使用前必须对照完整配置核实。
2. **像素内烧录注释/水印（burned-in annotations）不检测、不移除** —— 需独立影像处理流程。
3. 输出**不等同于合规认证**（HIPAA Safe Harbor / GDPR 匿名化 / 机构 IRB 要求）。
4. UID 重映射为确定性哈希；不保存/不输出映射表。
5. NIfTI 等格式转换本身**不是**去标识化（且丢失元数据）。

## 4. 验证方法（selftest 覆盖）

- 原始 PHI 字节串在输出中零出现（逐串检查）。
- 全部输出 UID 以私有前缀 1.826.0.1.3680043.8.498 开头且 remap 函数可复现。
- PatientSex 保留、PatientName/PatientID 置空且标签仍在（Type 1 不删除）。
- 私有标签计数归零。
- 像素字节逐字节不变（含封装结构原样复制）。
- 声明标签存在且 item 内容 = 113040/DCM。
- 隐式/显式/封装三种输入全部可回读、无警告。
