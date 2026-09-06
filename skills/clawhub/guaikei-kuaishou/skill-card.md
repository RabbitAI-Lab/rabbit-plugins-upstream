## Description:

Collects public Kuaishou data by keyword, creator profile, or video link and returns structured JSON for content research, competitor monitoring, KOL screening, comment insight, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, MCN operators, analysts, and developers use this skill to search public Kuaishou videos, list a creator's public posts, and retrieve public video comments for downstream summaries, comparisons, reports, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou query or link inputs and GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Confirm the data-sharing and authorization scope before use, and configure the token only in trusted environments.

Risk: Successful command results may be saved locally under logs.

Mitigation: Review log retention practices and delete local logs when they are no longer needed.

Risk: The skill is limited to public Kuaishou data and can return empty or error statuses for unavailable, deleted, private, or invalid inputs.

Mitigation: Check the returned status and error code before drawing conclusions, and retry with valid public links or broader keywords when appropriate.

## Reference(s):

- [Guaikei Kuaishou on ClawHub](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from the command-line tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; successful results may be saved locally under logs.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
