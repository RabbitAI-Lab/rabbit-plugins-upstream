## Description:

用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析，覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve read-only Douyin work details by aweme ID or content URL for content research, interaction-metric review, and structured analysis of video or image/text posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin content URLs or IDs to SocialDataX and requires SOCIALDATAX_API_KEY at runtime.

Mitigation: Install and use it only when the user is comfortable sharing those inputs with SocialDataX and providing the API key in the runtime environment.

Risk: Optional media download commands can write media files locally.

Mitigation: Use explicit user-selected output paths or directories and review saved files after download.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON data from the SocialDataX CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail lookups; optional media download commands can write files to user-selected local paths.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
