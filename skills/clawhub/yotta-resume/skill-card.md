## Description:

元简 — 本地求职者简历诊断、单轮模拟面试与成品导出技能：分析简历结构、经历证据、量化指标、岗位匹配和风险，向用户追问缺失事实，给出逐条合理化修改建议，并运行由简历证据、JD 缺口和来源题库共同驱动的模拟面试与复盘，把确认后的内容导出为 DOCX/PDF。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Job seekers use this skill to review resume evidence and structure, compare a resume with a job description, clarify missing facts, practice a single-round interview, and export a confirmed resume.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags unpinned install commands and maintenance capabilities not described in the skill summary; the scan was partial.

Mitigation: Review the package version and source before installing, and avoid unpinned install commands until they have been checked.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-resume)
- [Usage guide](artifact/references/usage.md)
- [Frequently asked questions](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown, JSON, DOCX, HTML, PDF]

**Output Format:** [Markdown or JSON reports, interview prompts and reviews, and resume files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes files locally; PDF input may require PyMuPDF and PDF output requires a Chromium-based browser.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
