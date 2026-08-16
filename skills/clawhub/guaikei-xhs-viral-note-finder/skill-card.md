## Description:

Retrieves public Xiaohongshu note, comment, keyword-search, and creator-post data for content research, competitor monitoring, KOL screening, and audience-feedback analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, market researchers, and data analysts use this skill to retrieve public Xiaohongshu data for viral-note discovery, competitor monitoring, KOL screening, trend research, and comment analysis. It is not for login-gated, private, posting, liking, following, or commenting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and embedded URL query tokens are sent to guaikei.com with the configured API token.

Mitigation: Use the skill only for authorized public-data research, avoid sensitive targets when data sharing is not acceptable, and confirm the token and service are approved for the workspace.

Risk: Command results are saved locally and may contain research targets, returned public data, or competitor-monitoring context.

Mitigation: Review generated logs after use and delete or secure them when the research context or returned data is sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-viral-note-finder)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API token and service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; commands return structured JSON and may save local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command inputs include Xiaohongshu keywords, note URLs, profile URLs, and limits.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
