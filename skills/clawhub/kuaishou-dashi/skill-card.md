## Description:

Kuaishou Dashi helps agents search Kuaishou public videos by keyword, fetch public creator post lists, and retrieve public video comments as structured JSON for content research, competitor monitoring, KOL screening, trend analysis, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, brand marketing teams, MCN teams, and analysts use this skill to collect and analyze public Kuaishou search results, creator posts, and video comments. It supports topic discovery, competitor monitoring, KOL screening, public-comment analysis, and trend reporting without logging into a Kuaishou account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party guaikei.com API token and sends Kuaishou search terms or URLs to that service.

Mitigation: Use only approved tokens and confirm the data-sharing scope is acceptable before running searches or URL lookups.

Risk: Fetched public data may be retained in local JSON logs.

Mitigation: Review local log retention needs and delete the logs directory on shared machines or when results should not remain on disk.

## Reference(s):

- [Kuaishou Dashi ClawHub Page](https://clawhub.ai/engheng-art/skills/kuaishou-dashi)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output includes status, error_code, request metadata, and result data when available; successful runs may also save local JSON logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
