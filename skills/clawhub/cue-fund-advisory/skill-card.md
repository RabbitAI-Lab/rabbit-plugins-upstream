## Description:

用 Cue 跑“基金投顾”场景的深度研究，帮助穿透公募基金底仓、分析基金经理能力与风格漂移、评估选股与择时能力，并产出基金遴选与投后跟踪可用的归因评估与配置建议底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External financial research users and advisors use this skill to run Cue fund-advisory research for asset allocation reports, public fund due diligence, fixed-income fund screening, performance attribution, and portfolio holding overlap analysis. Outputs are research drafts with source links and should support, not replace, professional diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Cue's online service and can consume Cue credits.

Mitigation: Require explicit user confirmation before running a selected research buddy or spending credits.

Risk: The runner reads the local Cue API key from the user's Cue configuration.

Mitigation: Install and run only in an environment where the user is comfortable granting Cue account access.

Risk: First-time setup may clone or update the external Cue runner repository.

Mitigation: Review the runner source and repository location before installation or update in controlled environments.

Risk: Fund research reports can be incomplete, stale, or unsuitable as standalone financial advice.

Mitigation: Treat outputs as sourced research drafts and preserve source links for independent review and professional diligence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-fund-advisory)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with source links and inline shell/API instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before spending Cue credits; final reports preserve source links.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
