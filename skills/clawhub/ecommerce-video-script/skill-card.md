## Description:

当用户需要根据商品信息撰写带货短视频、商品演示或种草口播脚本时使用。提供商品链接或商品资料，输出分镜、口播、演示动作与行动引导；可按需参考同类商品。在线商品能力支持抖音与小红书，已有资料可直接写作。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商商家、内容创作者及营销人员，依据用户提供或经支持的平台查询到的商品资料，编写可拍摄的短视频带货脚本。脚本可包含分镜、口播、演示动作、字幕、行动引导和待核实信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI runs an unpinned package at @latest that may change between uses and may access configured credentials.

Mitigation: Review the package and command before execution, and run it only in an environment with the intended credential scope.

Risk: The skill does not disclose whether product lookup inputs are sent to SocialDataX, and the security review reports incomplete scan coverage.

Mitigation: Confirm the service's data-handling terms before sending sensitive product or business information.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/ecommerce-video-script)
- [SocialDataX product and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a time-coded script table, shoot preparation, fact sources, and items to verify]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the requested duration, audience, platform, tone, and filming conditions; defaults to 30 seconds when duration is unspecified. Does not generate or publish video.]

## Skill Version(s):

0.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
