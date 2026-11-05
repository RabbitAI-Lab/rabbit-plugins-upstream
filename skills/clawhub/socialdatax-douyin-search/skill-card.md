## Description:

用于检索抖音热榜及视频、图文作品，支持关键词发现、内容调研、竞品分析和趋势研究。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向进行抖音内容调研的用户，用于查看热榜、搜索视频和图文作品，并发现关键词、竞品及趋势。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and usage attribution are sent to SocialDataX and may consume credits.

Mitigation: Avoid confidential search terms and review expected credit use before querying.

Risk: The API key and external CLI package carry ordinary credential and package-installation risks.

Mitigation: Keep the API key in a protected secret store and use a reviewed, pinned CLI release with only the credentials it needs.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis, Text]

**Output Format:** [JSON search results with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may be paginated; summaries can include visible ranking, content, author, and engagement details.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
