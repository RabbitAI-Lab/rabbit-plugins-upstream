## Description:

Retrieves public Douyin search results, creator posts, video comments, and hot-list data for topic research, competitor monitoring, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content or marketing analysts use this skill to fetch structured public Douyin data for keyword research, creator monitoring, comment analysis, trend tracking, and downstream reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, links or IDs and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when third-party API data sharing is acceptable, restrict routing to explicit Douyin-related requests, and keep the token out of shared logs and screenshots.

Risk: Local JSON logs may retain collected public data or reveal research activity.

Mitigation: Delete or manage the skill's local logs when retrieved data or analysis activity should not persist on disk.

Risk: The skill is intended for public Douyin data and does not support private, hidden, or login-only data.

Mitigation: Use only public Douyin links, IDs, or keywords and stop if the request asks for private or account-authenticated access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-search-keyword)
- [Guaikei Douyin data API](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON results with optional concise Markdown summary and local JSON logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; logs are written under the skill's local logs directory.]

## Skill Version(s):

1.2.2 (source: evidence release metadata, frontmatter metadata, package.json, changelog released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
