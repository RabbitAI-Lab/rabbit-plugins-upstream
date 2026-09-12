## Description:

Collects public Kuaishou video, creator post, and comment data through Guaikei API commands and returns structured JSON for content research, competitor monitoring, KOL discovery, comment insight, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, brand marketers, MCN teams, market analysts, and developers use this skill to search Kuaishou videos, retrieve public creator posts, and collect video comments for structured downstream analysis. It supports content ideation, competitor monitoring, KOL screening, comment insight, and trend reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, and related requests are sent to the Guaikei API using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when this external data sharing is acceptable and avoid submitting sensitive topics or URLs.

Risk: Successful results are saved locally in plaintext logs that may include searched topics, profile URLs, video URLs, comments, and creator data.

Mitigation: Review or delete the logs directory after use when results should not remain on disk or be committed or backed up.

Risk: The skill only supports public Kuaishou data and can return empty or error statuses for unavailable, private, deleted, rate-limited, or unauthorized requests.

Mitigation: Check status and error_code before drawing conclusions, retry only where appropriate, and do not treat empty results as successful evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-public-content-collector)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful command results are also written to local plaintext JSON logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
