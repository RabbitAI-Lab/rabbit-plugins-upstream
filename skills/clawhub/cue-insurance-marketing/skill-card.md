## Description:

用 Cue 跑「保险营销」场景的深度研究：横向比对目标保险产品与竞品在保障、收益、服务与适配场景上的差异，扫描热点事件自动映射保险需求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

保险营销和客户沟通人员用该 skill 运行 Cue 深度研究，用于保险产品对比、营销线索生成、产品适当性核查、条款理解和销售合规边界梳理。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Cue's hosted research service and may spend Cue credits.

Mitigation: Require explicit user confirmation before running paid research, as the artifact instructs.

Risk: The setup flow may clone or update the Cue runner in ~/.cue.

Mitigation: Install only when the user accepts the local runner setup and is comfortable with the referenced Cue repositories.

Risk: Generated insurance marketing material may be mistaken for legal, compliance, underwriting, or financial advice.

Mitigation: Treat outputs as research support and review them against applicable insurance, suitability, and compliance requirements before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-insurance-marketing)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner repository mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown reports with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cue account access and explicit user confirmation before spending credits.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
