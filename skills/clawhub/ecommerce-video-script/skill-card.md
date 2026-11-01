## Description:

根据商品资料或支持平台的商品信息生成带货短视频脚本，包括分镜、口播、演示动作与行动引导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、商家和营销人员可依据商品资料撰写可拍摄的带货短视频脚本；脚本包含分镜、口播、演示动作和行动引导，并标出信息来源与待核实事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online product lookups share supplied links, IDs, or search terms with SocialDataX and may consume paid credits.

Mitigation: Use supplied product materials when they are sufficient; before an online lookup, make clear that product details are shared with SocialDataX and may use paid credits.

Risk: CLI dependencies and API credentials introduce software supply-chain and secret-handling risks.

Mitigation: Prefer a reviewed fixed CLI version over @latest, keep SOCIALDATAX_API_KEY private, and do not include the key in generated files.

## Reference(s):

- [SocialDataX API key information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-video-script)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a storyboard table, spoken script, shot directions, captions, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided duration, audience, platform, tone, and filming constraints; defaults to 30 seconds when duration is unspecified.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
