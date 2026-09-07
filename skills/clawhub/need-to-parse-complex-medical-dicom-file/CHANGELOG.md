# CHANGELOG — need-to-parse-complex-medical-dicom-file

## v2.0.0 (2026-09-06)

### v1.0.6 缺陷清单（发布前审计）
1. 空心存根：SKILL.md 正文仅 Detection/Mitigation/Verification 三句声明，零脚本/零数据/零参考 —— 声称"处理复杂医学 DICOM"但无任何可执行能力（能力幻觉）。
2. 版本漂移：frontmatter 1.0.0 vs 注册表 1.0.6。
3. 依赖幻觉：README 声称 "Requires python3 + pydicom"，实际不捆绑任何东西（纯声明，用户照做会装错方向 —— v2 恰恰是零第三方依赖）。
4. "Complete Skill Reference (Unchanged)" 段落复述同一空壳，无任何可验证内容。
5. 无 PHI/去标识化实质、无测试、无能力边界声明（压缩像素等）。

### 依据（全部 2026-09-06 在线核对）
- DICOM PS3.5 2026c（NEMA）：part05.html TOC —— §6.2 VR、§7.1.2 Explicit、§7.1.3 Implicit、§7.2 Group Length、§7.5 序列（item/delimitation/显式 VR 继承）、§7.8 私有、§8.2 封装像素。
- DICOM PS3.15 2026c（NEMA）：part15.html —— §6.9 Attribute Confidentiality Profiles、Annex E Basic Profile（300+ 标签，动作码 D/Z/X/K/C/U）。
- Transfer syntax UID 表：meddream conformance（2020-08-19）+ Gdcm 3.0 ConformanceSummary + postdicom 综述，三方交叉核对。
- 去标识化实践：micheledpierri（2026-07-19）、healthcareonlinetools（2026-03-17）、fast.io（2026-04-22）：私有标签=最常见泄漏源；日期按 VR 清洗；UID 一致性重映射；burned-in 注释需独立处理。
- pylibjpeg 2.1.0（GitHub README/PyPI）：解码插件分工与 pydicom 命令（诚实指向）。

### 设计决策
- 纯 stdlib（argparse/hashlib/json/os/struct/sys）；离线；确定性（gen/deid 同输入同字节）。
- 诚实边界：压缩像素检测+报告+exit 2+精确 pylibjpeg 命令；绝不猜测像素值。
- deid = PS3.15 Basic Profile 直接标识符子集（约 20 标签 Z/X + 全部私有 X + DA/DT/TM 按 VR + 全部 UID SHA-256 确定性重映射 + (0012,0062)/(0012,0063) 声明），输出固定携带 limitations（不等同合规认证；burned-in 不移除）。
- 退出码纪律：0 成功 / 2 输入错误与诚实拒绝 / 3 check 有 error；错误 JSON → stderr。
- token 经济：summary 紧凑 JSON 为默认；parse --tags 过滤；每条输出带 purpose="技术检查，不用于诊断"。

### 自检
- `scripts/selftest.py`：102 项检查 / 10 组（G1 生成器确定性 · G2 显式解析 · G3 隐式解析 · G4 封装检测 · G5 像素导出逐像素 · G6 诚实拒绝 · G7 check 语义 · G8 deid PHI 清零 · G9 UID/声明 · G10 隐式/封装 deid · G11 CLI 契约与文档幻影）。
- 最终结果：102/102 PASS（离线、确定性、合成数据，无 PHI、无网络）。

### 审计轨迹（多模型对抗审计，全部完整文件入 prompt、无截断）

**Pass-1（3 模型，跨 3 家 provider；cohere trial 键 429 降级后 parser 审计由 llm7 复核）：**

| 审计 | 模型/provider | 域 | 结果 |
|---|---|---|---|
| A | cohere command-a-03-2025 | 字节级解析/序列化（PS3.5） | FINDINGS: 0 |
| A2 | llm7（A 的独立复核） | 同上 | FINDINGS: 0（逐项确认元素布局/VR/序列/封装 4 字节片段/meta 长度/PNM 16 位大端/生成器填充） |
| B | llm7 | deid vs PS3.15 + 诚实契约 + 退出码 | 0 缺陷（3 点均为合规确认） |
| C | gemini | 幻影声明 + selftest 缺口 + 参考事实 | 3 项：1 采纳 2 驳回 |

C 项 triage（byte+run 验证）：
- **C1**（"selftest 未证明 check 输出 encapsulated_pixel_data"）→ **驳回**：selftest G4 恰断言该 code 且 102/102 通过（运行验证，非引文推断）。
- **C2**（"封装桩缺 Basic Offset Table"）→ **驳回**：PS3.5 §8.2 偏移表为空时可省略；文件明确标注合成检测桩（fragment 为不可解码 STUB，工具设计上从不解码）。
- **C3**（"值类型映射未写入 SKILL 契约"）→ **采纳**：SKILL.md 增加"值类型约定"段。

**Pass-2（2 模型 diff 复审：pass-1 后的唯一 delta = SKILL.md 值类型段 + --bits 行）：**
- P2a/gemini：2 LOW（文档精度：多值 IS 不拆分、UI 去尾 NUL 未写明）→ **已修**；C1/C2 驳回判定复核为"defensible"；--bits 无新幻影；无 JSON 契约破坏。
- P2b/llm7：FINDINGS: 0（值类型段与代码行为逐项一致；C1/C2 驳回成立；无幻影；无契约破坏）。

**审计期间同步修复的自身 bug（byte-verify 发现，非模型报告）：** OW 像素在 parse 输出中的实际形态（hex 预览）与文档不符 → 契约行改写；`--tags` 语法歧义（`0010,0020` 逗号冲突）→ 改为 nargs 每参一标签；8 位 PNM 头长 13 字节（selftest 偏移笔误）。

**Provider 可用性注记（2026-09-06）：** mistral（全键 429）、zai（单键 429）不可用；openrouter 冷却至 09-07 晚；故跨 3 家可用 provider（cohere/llm7/gemini）完成双轮审计。

### 交付校验
- 最终自检：**102/102 PASS**（`python3 scripts/selftest.py`，离线、确定性）。
- 性能：525 KB（512×512×16-bit）文件各命令 <100 ms。
- **TREE-SHA256-v1：f9027e167db46348aa39cd721c17723fde34a9a241fea261bbda39ff1880b75b（8 文件）**
  算法：每文件 entry=`<relpath>|<sha256(bytes)>`，按 entry 排序后 `sha256("\n".join)`；
  排除 readme.md/skill-card.md/_meta.json/.published/.DS_Store 与 .git/.clawhub/__pycache__/.pytest_cache。

