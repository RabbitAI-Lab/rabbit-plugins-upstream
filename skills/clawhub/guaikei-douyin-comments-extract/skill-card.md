## Description:

Supports Douyin keyword search, creator post retrieval, video comment analysis, and real-time hot list lookup for content research, competitor monitoring, public sentiment analysis, trend tracking, viral content discovery, and Douyin operations analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and analysts use this skill to retrieve structured public Douyin data for keyword research, creator post tracking, comment analysis, hot trend monitoring, and downstream content or marketing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, links, IDs, requested limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use only when that third-party API flow is acceptable, keep the token secret, and avoid committing it to scripts or dotfiles.

Risk: Fetched comments and account or content metadata may be retained in generated local logs.

Mitigation: Review or delete the generated logs directory when collected data should not be retained locally.

Risk: The skill is limited to disclosed, read-only public Douyin data retrieval through the configured API.

Mitigation: Do not use it for private, hidden, login-gated, or write-action workflows; stop and ask for different authorization or tooling instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-comments-extract)
- [Guaikei API and token service](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot list CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON on stdout with concise agent-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; logs and fetched results may be saved locally by the skill.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
