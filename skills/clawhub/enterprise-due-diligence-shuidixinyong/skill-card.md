## Description:

基于招投标记录和公开信息，为合作前的企业审查生成单公司或双公司尽调报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users assessing a prospective customer, supplier, or partner use this skill to review bidding activity, commercial relationships, competitors, and sourced public-risk information before collaboration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shareable reports may contain login-bypass links, company intelligence, or contact details.

Mitigation: Review reports and links before sharing outside your account or organization.

Risk: Opt-in auto-registration uses a device hash and stores a service credential.

Mitigation: Supply an API key manually if device-based registration is not acceptable; protect stored credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong)
- [Skill workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [API quick reference](artifact/references/api-quick.md)
- [Registration and credential handling](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML]

**Output Format:** [Conversational summary and Markdown report, with a shareable HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-company reports and two-company comparisons with source links.]

## Skill Version(s):

1.0.6 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
