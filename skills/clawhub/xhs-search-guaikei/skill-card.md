## Description:

Retrieves structured public Xiaohongshu note, author, interaction, comment, and creator-post data for content planning, competitor monitoring, KOL screening, and marketing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketing teams, analysts, and operations teams use this skill to collect public Xiaohongshu search, note detail, comment, and creator-post data before producing content strategy, trend, competitor, KOL, or sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, links, and GUAIKEI_API_TOKEN to the Guaikei API.

Mitigation: Use only when third-party API processing is acceptable, avoid sensitive research terms on shared systems, and rotate the token if it is exposed.

Risk: Returned Xiaohongshu data is saved under the skill's local logs directory.

Mitigation: Review log retention, file permissions, and cleanup practices before using the skill with sensitive business research.

Risk: The tool retrieves public data and does not replace compliance or platform-use review.

Mitigation: Confirm the intended use is limited to authorized public-data analysis and do not use outputs for prohibited redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-search-guaikei)
- [Guaikei API website](https://www.guaikei.com)
- [Parameter and invocation guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON written to stdout and saved as local log files, with concise agent guidance around command selection and failures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supported commands cover keyword search, note detail, comments, and creator posts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
