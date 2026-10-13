## Description:

按行业和地区扫描工程拟建项目、采购意向与临期续约机会，并生成按价值排序的商机清单和跟进建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

工程建设领域的业务开发人员按行业、产品和地区发现早期项目线索、采购意向及即将续约的项目，确定跟进优先级。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and a device-derived MAC hash are sent to the provider during auto-registration.

Mitigation: Review the data-sharing implications; use an existing API key to skip registration, or obtain consent before registering.

Risk: The skill saves an API credential in a persistent local configuration file.

Mitigation: Restrict access to the credential file and avoid sharing its contents.

Risk: Exported HTML reports can contain clickable access links that bypass login.

Mitigation: Treat reports and sk-bearing URLs as sensitive; review access links before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar)
- [API quick reference](references/api-quick.md)
- [Registration and credential setup](references/auto-register.md)
- [Report template](references/report-template.md)
- [Scanning workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML reports, Guidance]

**Output Format:** [Prioritized Markdown opportunity list; optional or full-scan HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and recommended follow-up actions.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
