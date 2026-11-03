## Description:

用于抖音达人数据、抖音达人作品、作品列表、图文列表、短剧/合集列表、近期发布、内容调研和创作者内容分析。覆盖 Douyin creator works and series，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, researchers, and marketers use this skill to review a Douyin creator's videos, image/text posts, or short-drama series for content research, benchmarking, and account tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external SocialDataX service and CLI requires trusting that provider and its software before supplying an API key.

Mitigation: Review the service and use a fixed, reviewed package version; keep the key in supported secret storage and out of chat and version control.

Risk: Unbounded page or item requests may increase usage costs.

Mitigation: Set page or item limits appropriate to the research task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured creator content and series data with textual summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content lists support pagination; available fields vary by returned content type.]

## Skill Version(s):

0.1.22 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
