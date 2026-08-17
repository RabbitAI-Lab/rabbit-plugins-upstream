## Description:

用 Cue 跑「私募尽调」场景的深度研究，汇总私募管理人登记、管理规模、核心团队、产品运作、股权结构、处罚涉诉等公开信息，产出带来源链接和疑点清单的尽调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, investment teams, and diligence reviewers use this skill to run Cue-assisted private-fund due diligence workflows over public data. It helps screen managers, products, affiliations, registration status, and regulatory or litigation concerns before review meetings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may clone or update an external Cue runner before use.

Mitigation: Review the Cue runner source and repository origin before installing or updating it in controlled environments.

Risk: The workflow uses a local Cue API key, contacts Cue services, and may send the user's research subject to those services.

Mitigation: Confirm account configuration and data-sharing expectations before running sensitive diligence queries.

Risk: Deep research consumes account credits after confirmation.

Mitigation: Require explicit user confirmation for the selected buddy, research subject, and credit-consuming run before execution.

Risk: The skill covers public-data research and does not replace formal diligence, legal review, underwriting, or compliance decisions.

Mitigation: Treat generated reports as evidence-gathering support and review source links and conclusions before business use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-private-fund-dd)
- [Publisher profile](https://clawhub.ai/user/wangxiaoxu)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with source links and inline shell commands for running the Cue research runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on live Cue playbook data, external public sources, account credentials, and available credits.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
