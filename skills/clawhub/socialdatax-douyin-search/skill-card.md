## Description:

用于查看抖音热榜、搜索视频与图文作品，并支持关键词、创作者和趋势调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户可用此 skill 查看抖音热榜、搜索视频和图文作品、发现创作者，并开展内容调研、竞品分析和趋势观察。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and usage attribution are sent to SocialDataX, and requests may consume credits.

Mitigation: Avoid confidential queries and set page or item limits appropriate to the task.

Risk: The exact npm package version executed by the documented @latest command is not fixed by the bundled artifact.

Mitigation: Prefer a reviewed fixed CLI version when repeatability matters.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search)

## Skill Output:

**Output Type(s):** [JSON data, Analysis]

**Output Format:** [SocialDataX search results as JSON with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; search calls may consume credits.]

## Skill Version(s):

0.1.21 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
