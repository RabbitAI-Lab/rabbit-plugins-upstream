## Description:

用 Cue 跑「融资融券」场景的深度研究：横向比对各主要券商的两融政策（折算率、标的覆盖、保证金、集中度），识别竞对抢客与风险收缩信号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or external users in securities research and brokerage workflows use this skill to run Cue deep research on margin-trading policy comparisons, competitor monitoring, ETF and technology-security financing terms, single-security policy checks, client-acquisition opportunities, and risk-tightening signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download or update the Cue runner in the user's home directory and contact Cue services.

Mitigation: Confirm the runner setup and network behavior before installation or execution.

Risk: The skill uses a local Cue API key and can spend Cue credits.

Mitigation: Require explicit user confirmation before each credit-consuming research run.

Risk: Margin-trading research outputs may be mistaken for investment, legal, compliance, underwriting, or due-diligence advice.

Mitigation: Treat outputs as public-data research support and route decisions through qualified review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-margin-trading)
- [Cue playbook API](https://cuecue.cn/api/playbook)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown research report with source links and inline shell commands for setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use public-data research results from Cue services and requires explicit confirmation before spending Cue credits.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
