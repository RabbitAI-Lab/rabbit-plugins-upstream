---
name: yotta-resume
slug: yotta-resume
version: 0.1.3
displayName: 简历诊断与成品导出·元简
summary: 简历诊断与成品导出（元简）：本地分析简历结构、经历证据和量化指标，按目标 JD 找出关键词缺口，追问缺失事实并给出逐条修改建议；确认后导出 DOCX / HTML / PDF。
description: '简历诊断与成品导出（元简）—— 本地读取 Markdown / DOCX 简历，分析章节结构、经历证据、量化指标、联系方式风险与目标 JD 关键词缺口；向求职者追问缺失事实，给出逐条合理化修改建议，并把确认后的同一份内容导出为 DOCX / HTML / PDF。触发：简历诊断、简历分析、改简历、简历追问、JD匹配、导出 Word / PDF。边界：不编造经历、数字或结果，不自动投递，不承诺 ATS、面试或 Offer 结果，不处理复杂设计作品集排版；默认本地处理且不联网。'
tags: [简历诊断, 简历分析, 简历优化, 改简历, 简历修改, 简历润色, 求职简历, JD匹配, 简历导出, Word简历, PDF简历, resume review, resume analyzer, resume export, job description matching]
category: office-efficiency
license: MIT
homepage: https://github.com/YottaMeta/yotta-resume
metadata:
  zh_name: "元简"
---
# 元简（yotta-resume）

元简先根据简历内容自动识别行业，再分析结构、经历证据和 JD 关键词覆盖，
提出可回答的高价值问题，并按用户确认的事实导出 DOCX、HTML 或 PDF。

## 触发与边界

- Triggers：用户要求诊断简历、改简历、补强经历证据、做 JD 匹配，或把已确认的简历导出为 Word/PDF。
- Do NOT trigger：用户要求代投简历、编造经历或数字、预测面试结果、评估受保护个人属性，或制作复杂设计作品集排版。

常见自然语言说法：

- “帮我看下这份安全运营简历哪里写虚了。”
- “照这个 JD 看我还缺哪些关键词和证据。”
- “先别改，告诉我还需要问我什么。”
- “把确认后的内容导成 Word 和 PDF。”
- “这段经历我只能确认范围，不能确认具体数字，应该怎么写？”

相近但不适用：“帮我海投”“把结果写成 90 分”“编一段大厂经历”“替我预测 Offer”。

## 核心流程

1. 首次安装或排查环境时先运行：

```bash
python scripts/yotta_resume.py doctor
```

`doctor` 会检查随包文件、数据契约、PyMuPDF、PDF 浏览器、临时目录和 Python 版本。
PDF 依赖是可选项：缺少时仍可使用 Markdown / DOCX 输入和 DOCX / HTML 输出。

2. 读取简历文件。支持 UTF-8 Markdown、UTF-8 文本、DOCX 和文字层 PDF。
   PDF 解析优先使用本地 PyMuPDF；缺少依赖、加密、损坏或扫描件时明确失败或降级，
   不生成伪完整报告。
3. 运行分析，优先让用户提供目标岗位 JD：

```bash
python scripts/yotta_resume.py audit --resume resume.md --jd jd.txt --format json
```

4. 阅读 `source_manifest`、`parse_warnings`、`issues`、`unknowns` 和 `questions`。
   先确认输入解析质量、规模、个人边界、结果、日期和 JD 缺口，再修改简历。
   用户没有确认的事实不要写进简历。
5. 按用户确认的信息修改 Markdown，再导出成品：

```bash
python scripts/yotta_resume.py export --input revised.md --docx revised.docx --html revised.html --pdf revised.pdf
```

6. 核对输出文件存在且可打开。多格式导出会先写入临时区，全部成功后一次性提交；
   任一格式失败时不会留下本次部分成品，也不会覆盖原有同名文件。
   PDF 依赖本机 Chromium、Chrome 或 Edge；未找到浏览器时命令会明确失败，不会生成伪 PDF。

7. 需要单独校验随包岗位族、证据账本、题库、来源和双角色权限契约时运行：

```bash
python scripts/yotta_resume.py contracts --format json
```

## 输出契约

- `audit`：JSON 或 Markdown，包含文件来源清单、解析提示、行业识别、章节识别、
  要点统计、工具发现、未知项、追问、修改建议、JD 匹配、结构准备度和边界声明。
- `export`：DOCX / HTML / PDF。三者来自同一份 Markdown 内容模型，联系方式保留在成品简历中。
- `contracts`：离线校验 `data/` 下的 6 个实际契约与 6 个 JSON Schema，
  失败返回退出码 `6`，不写文件、不联网。
- `doctor`：返回 `PASS / WARN / FAIL`，核心文件或契约失败返回退出码 `6`；
  PyMuPDF 或浏览器缺失只记为 `WARN`，不阻断 DOCX / HTML 路径。
- 分析报告：手机号和邮箱会被打码；不承诺 ATS、面试或 Offer 结果。

## 评分与数字护栏

- `readiness.score` 的展示名称固定为“结构准备度（规则分）”，
  `score_type` 为 `structure_rule_score`，只反映章节、量化证据、文本清洁度和
  可选 JD 关键词覆盖，不是招聘方评分。
- 只能原样引用工具返回的数值；**不得改写为其他数值、主观数字区间或“实际分数”**。
  需要对招聘方视角作判断时，只允许定性标签并列出简历证据。
- 未提供 JD 时 `jd_match.coverage` 必须为 `null`，报告写明不能判断岗位匹配。
- `jd_match` 使用版本化固定词表，只检查明确关键词，不做语义匹配或岗位排名；
  必须同时展示 `lexicon_version` 和 `limitations`。
- 报告必须区分“工具规则发现”“智能体复核发现”“待用户确认事实”。
  智能体额外发现不得冒充工具输出，且必须引用简历原文或来源页。
- 规则不能判断招聘竞争力、面试通过率或 Offer 结果；必须列入 `unknowns`。

## 行业扩展

- `industry_detection` 根据简历明确关键词识别行业，只使用可见内容，不读取受保护属性。
- 当前可区分网络安全、软件研发、数据与人工智能、业务运营和通用兜底。
- 网络安全已有 6 个岗位族和 18 道种子题；其他行业暂用通用证据与追问维度。
- 新增行业时扩展 `data/industry-registry.json` 及 Schema，不需要修改主分析流程。
- 多个行业信号接近时 `status=ambiguous`，不得自行猜测行业。

## 渐进披露

- 详细输入格式、CLI 退出码和浏览器要求见 [references/usage.md](references/usage.md)。
- 常见问题见 [references/faq.md](references/faq.md)。
- 自然语言说法见 [references/trigger-examples.md](references/trigger-examples.md)。
- 端到端工作流见 [references/workflow-examples.md](references/workflow-examples.md)。
- 行业、岗位族、题库、来源与 HR 权限契约见 [references/data-contracts.md](references/data-contracts.md)。

## 自检

```bash
python scripts/yotta_resume.py doctor
```

源码仓库维护者运行完整自动化测试；测试文件不作为终端用户运行前提。
