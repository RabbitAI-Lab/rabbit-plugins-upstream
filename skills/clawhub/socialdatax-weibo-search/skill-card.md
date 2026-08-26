## Description:

用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究，并覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, researchers, and content teams use this skill to retrieve current Weibo hot-search lists and keyword post results, then summarize visible ranking signals and post evidence for trend, competitor, and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI package and the external SocialDataX service using SOCIALDATAX_API_KEY.

Mitigation: Install and run it only in environments where that package and service are trusted, and provide the API key through environment-secret handling rather than embedding it in files.

Risk: Weibo research queries and returned data are retrieved through SocialDataX rather than directly from local browser or account data.

Mitigation: Treat results as externally sourced research data, preserve cited post IDs and URLs for traceability, and avoid using the skill for login, posting, liking, commenting, or account changes.

Risk: Multi-page search uses opaque pagination tokens that can break result continuity if altered.

Mitigation: Pass returned next-page tokens back unchanged within the same keyword pagination chain and keep observed evidence separate from interpretation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON-derived evidence and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Weibo post IDs, URLs, authors, interaction counts, publish times, and pagination markers when traceability is needed.]

## Skill Version(s):

0.1.18 (source: server evidence release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
