## Description:

XHS Dashboard Build helps agents search public Xiaohongshu notes, retrieve note details and comments, and collect public creator posts for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content teams, and market analysts use this skill to fetch structured public Xiaohongshu data for topic discovery, note and comment review, creator monitoring, competitor research, and downstream summaries or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, public note or profile URLs, and the GUAIKEI_API_TOKEN are sent to the Guaikei service.

Mitigation: Install and run the skill only when that third-party API use is acceptable, and scope the token to the intended research workflow.

Risk: Command results are written to local logs and may contain retained market, competitor, creator, or comment research data.

Mitigation: Protect, review, or delete the logs directory according to the sensitivity and retention needs of the research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-dashboard-build)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful CLI calls write structured JSON logs locally.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
