## Description:

Fetches structured public Kuaishou video search results, creator post data, and video comments for competitor research, content analysis, topic research, and brand content investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, brand teams, MCNs, content operators, and creators use this skill to query public Kuaishou data for keyword research, competitor monitoring, creator post review, and comment analysis. The skill routes requests to Node.js commands that return structured JSON for downstream analysis, reporting, or comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou search terms, profile links, video links, and the GUAIKEI_API_TOKEN to the third-party guaikei.com API.

Mitigation: Use the skill only when that data sharing is acceptable, treat GUAIKEI_API_TOKEN as a secret, and rotate or revoke the token if exposure is suspected.

Risk: Fetched comments, account data, and research results are saved locally under logs/.

Mitigation: Review local log retention practices and delete logs when the collected public data should not be retained.

Risk: The skill is intended for public or authorized Kuaishou research and does not support private, hidden, or logged-in data.

Mitigation: Restrict use to public or authorized data collection and avoid using returned data for unlawful distribution or unauthorized profiling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-search-detail-fetcher)
- [Guaikei API Service](https://www.guaikei.com)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; command results include status, error_code, request metadata, skill metadata, and results, and are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata, SKILL.md metadata, package.json, and changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
