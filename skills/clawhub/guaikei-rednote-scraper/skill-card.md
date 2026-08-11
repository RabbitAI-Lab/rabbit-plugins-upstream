## Description:

Fetches public Xiaohongshu/RedNote search results, note details, comments, and creator post lists as structured data for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, content creators, and analysts use this skill to collect public Xiaohongshu/RedNote content data for topic discovery, competitor monitoring, comment analysis, creator tracking, and market trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Xiaohongshu keywords or links and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when that data sharing is approved, and verify token authorization before running commands.

Risk: Successful runs save fetched data as JSON files under the skill's logs/ directory.

Mitigation: Delete result files when they are no longer needed, especially on shared or backed-up machines.

Risk: The skill is intended for public Xiaohongshu/RedNote data and does not support private, hidden, or login-only content.

Mitigation: Reject requests for non-public data and keep downstream use within the user's authorization and policy requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-scraper)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command runs require Node.js and GUAIKEI_API_TOKEN; successful runs save JSON result files under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata and generated release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
