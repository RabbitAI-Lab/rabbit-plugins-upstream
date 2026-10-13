## Description:

分析医疗类招标项目的采购历史、潜在竞争者、历史成交价和投标风险，生成投标决策报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

医疗器械供应商和投标团队可针对具体医院采购项目评估是否参投、潜在竞争、建议报价及资格与废标风险。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may contain signed links that open protected pages without normal login.

Mitigation: Treat exported reports as sensitive; share only with intended recipients and avoid public posting.

Risk: Project and company search terms are sent to Zhiliaobiaoxun.

Mitigation: Avoid submitting confidential search terms unless sharing them with the service is acceptable.

Risk: Trial registration uses platform, CPU architecture and MAC-hash data; an API key and reports are stored locally.

Mitigation: Require consent before registration, use an existing key to skip device registration, and protect local credentials and reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/medical-device-bid-decision)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API quick reference](references/api-quick.md)
- [Analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML report]

**Output Format:** [Markdown decision report; optional self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source citations and may include shareable signed links to protected pages.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
