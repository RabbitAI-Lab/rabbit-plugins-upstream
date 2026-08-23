## Description:

Collects public Douyin search results, creator posts, video comments, and hot-trend data through CLI commands for content research, competitor analysis, comment insight, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to run Douyin-focused data collection workflows for public keyword search, creator-post collection, comment analysis, and real-time trend review. It is suited to content research, competitor monitoring, marketing analysis, and trend tracking when Douyin public data is intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin data-collection requests to a third-party guaikei.com API.

Mitigation: Install and run it only when that third-party API is intended and approved for the user's task.

Risk: The GUAIKEI_API_TOKEN is sensitive.

Mitigation: Provide the token only through the environment, avoid committing or sharing it, and rotate it if exposure is suspected.

Risk: Generated logs may contain research topics, account targets, video URLs, comments, and returned media links.

Mitigation: Review log contents after use, store them only in appropriate workspaces, and periodically delete logs that are no longer needed.

Risk: The trigger scope can apply to broad short-video research prompts and may return Douyin results when the user expected a generic search.

Mitigation: Use the skill only when the user explicitly wants Douyin or public Douyin data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-search-collect-export-videos)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [CLI commands and structured JSON responses, with JSON logs written to files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14.0 and a GUAIKEI_API_TOKEN environment variable; single requests may request up to 10000 records.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
