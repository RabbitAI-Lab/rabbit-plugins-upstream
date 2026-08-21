## Description:

建筑工程商机雷达帮助代理按行业、产品和地区发现建筑施工、市政、装修、园林、公路、房建和基建项目的早期商机，并输出按价值排序的线索清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commercial teams use this skill to scan construction-related opportunity sources for proposed projects, procurement intentions, and expiring service contracts. It supports early account planning by producing prioritized opportunities, follow-up suggestions, and optional HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and store account credentials and may expose login-bypass links in chat or exported HTML reports.

Mitigation: Install only when the provider is trusted, avoid sharing generated reports or sk-bearing links broadly, and review exported files before distribution.

Risk: The skill may collect a hashed device identifier after consent during automatic registration.

Mitigation: Use a preconfigured ZLBX_API_KEY to skip automatic registration, or proceed only after the user accepts the disclosed collection behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration workflow](artifact/references/auto-register.md)
- [知了商机大师](https://agent.zhiliaobiaoxun.com)
- [百炼标书](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, HTML files, Guidance]

**Output Format:** [Markdown opportunity list with optional generated HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based account registration; reports may include provider login-bypass URLs returned by the API.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
