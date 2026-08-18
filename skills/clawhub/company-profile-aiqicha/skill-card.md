## Description:

基于知了标讯招投标数据，为习惯使用爱企查等平台查企业的用户生成企业实力画像、客户供应商关系、竞争格局、公开风险和可分享报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, sales teams, procurement reviewers, and business researchers use this skill to investigate a company from a public bidding and contract-record perspective. It supports single-company intelligence reports and two-company comparisons covering business direction, bidding strength, customer and supplier relationships, competitors, and public risk signals.

### Deployment Geography for Use:

Global, with data sources and workflows focused on Chinese public bidding and procurement records.

## Known Risks and Mitigations:

Risk: The skill persists API credentials for later use.

Mitigation: Prefer a manually provisioned ZLBX_API_KEY where possible and avoid pasting or exposing API keys in chat, reports, or shared files.

Risk: Generated reports and API-returned URLs may contain signed access links.

Mitigation: Share HTML reports and links only with trusted recipients, and treat `sk` and auto-login URLs as access-bearing links.

Risk: Company research may involve sensitive commercial context.

Mitigation: Review the skill before installation in sensitive workflows and verify generated conclusions against the cited public bidding and risk sources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha)
- [Workflow Reference](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Auto Registration Reference](references/auto-register.md)
- [Report Template](references/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report in chat plus an optional self-contained HTML report file; may include concise configuration and account guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or user-approved auto-registration; generated reports may include signed access links returned by the API.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
