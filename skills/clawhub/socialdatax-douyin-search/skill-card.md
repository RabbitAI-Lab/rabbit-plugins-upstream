## Description:

用于抖音数据分析、抖音热榜、抖音作品搜索、图文搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Douyin hot search and work search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize Douyin hot-search, video, and image/text post data for keyword discovery, content research, competitor analysis, and trend scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin research queries through SocialDataX using SOCIALDATAX_API_KEY.

Mitigation: Keep the API key in the runtime environment, avoid placing secrets in files or prompts, and review query content before sending sensitive business research.

Risk: The preferred npx examples fetch socialdatax-skills@latest, which may execute a newer published package than the artifact was reviewed against.

Mitigation: Confirm the SocialDataX npm package is acceptable before installation, and use an organization-approved or pinned package version when reproducibility is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Douyin content IDs, URLs, titles or descriptions, authors, counts, publish times, content type, pagination markers, and observed ranking signals.]

## Skill Version(s):

0.1.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
