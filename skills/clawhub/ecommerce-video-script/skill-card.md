## Description:

当用户需要根据商品信息撰写带货短视频、商品演示或种草口播脚本时使用。提供商品链接或商品资料，输出分镜、口播、演示动作与行动引导；可按需参考同类商品。在线商品能力支持抖音与小红书，已有资料可直接写作。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、商家及营销团队可根据用户提供或在线获取的商品资料，制作带货短视频、商品演示或种草口播脚本，并整理需要核实的商品事实。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online product lookups send product URLs, IDs, or search terms to SocialDataX and may consume paid credits.

Mitigation: Use supplied product information for offline writing when possible, and make online lookups only when appropriate for the task.

Risk: The skill has ordinary software dependency risks when using online product lookups.

Mitigation: Use a reviewed exact CLI version and limit its access to the required API key and task files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/ecommerce-video-script)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown script table with timing, visuals/actions, voice-over, on-screen captions, and filming or fact-check notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied product information when available; otherwise supports optional product lookups for Douyin and Xiaohongshu. Defaults to a 30-second script when no duration is given.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
