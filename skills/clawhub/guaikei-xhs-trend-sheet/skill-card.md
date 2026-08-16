## Description:

Retrieves public Xiaohongshu notes, note details, comments, and creator posts as structured data for trend discovery, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, content operators, data analysts, and agent users use this skill to collect public Xiaohongshu data for content research, trend monitoring, competitor review, KOL screening, and comment analysis. It should not be used for login, publishing, engagement actions, private content, hidden content, or other data outside the documented public-data boundary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Xiaohongshu search terms or links are sent to guaikei.com with the configured API token.

Mitigation: Use the skill only when that third-party data transfer is acceptable and avoid submitting private, hidden, login-gated, or otherwise sensitive content.

Risk: Returned Xiaohongshu results may be saved locally in logs and can include comments, creator profile data, or competitive research records.

Mitigation: Review generated logs after use and delete them when they are no longer needed.

Risk: The skill is documented for public-data retrieval only and does not cover account login, publishing, liking, commenting, or private-data access.

Mitigation: Keep usage within the documented public-data boundary and do not use the skill for account actions or private content retrieval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-trend-sheet)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0+; command results may be written to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
