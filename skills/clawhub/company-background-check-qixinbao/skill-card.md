## Description:

基于招投标数据生成企业背景调查或双公司对比报告，涵盖主营业务、客户与供应商、中标实力、竞争格局及公开风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

企业采购、销售及投标团队可按公司名称调查中国企业的公开招投标表现、客户关系与竞争对手，或比较两家公司以辅助尽调。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional account setup uses a hashed MAC-derived device identifier and stores a persistent API key locally.

Mitigation: Obtain consent before registration, or provide an existing API key to skip it; protect the local credential file.

Risk: Shareable HTML reports and URLs with sk or sid parameters may grant access to report data or linked records.

Mitigation: Keep reports and access-bearing links private, and review them before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao)
- [API quick reference](artifact/references/api-quick.md)
- [Investigation workflow](artifact/references/workflow.md)
- [Report templates](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML files]

**Output Format:** [Conversational report and locally saved HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-company and two-company reports with source links; HTML reports may contain access-bearing links.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
