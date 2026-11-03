## Description:

根据用户提供的商品资料，或按需查询抖音与小红书商品信息，生成包含分镜、口播、演示动作与行动引导的带货短视频脚本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营人员、内容创作者和商家，根据商品事实、受众、平台与视频时长编写可拍摄的带货短视频脚本；用户明确需要同类参考时，也可查询抖音或小红书商品信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional online product lookups send product identifiers, URLs, or search terms to SocialDataX and may consume paid credits.

Mitigation: Use product information supplied by the user when it is sufficient; make online lookups only when requested and explain that they share the submitted product details and may use paid credits.

Risk: The external CLI package is outside the supplied artifact, so its code was not reviewed here.

Mitigation: Prefer a reviewed, pinned CLI version and store credentials using the client’s supported secret storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-video-script)
- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown table with time-coded scenes, visuals and actions, spoken lines, subtitles, and filming notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the requested duration (defaults to 30 seconds when unspecified); distinguishes supplied or retrieved product facts from items that still need verification.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
