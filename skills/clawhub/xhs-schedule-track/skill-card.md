## Description:

A XiaoHongShu operations data skill for searching public notes, retrieving note details and comments, and collecting public creator post lists for trend research, competitor analysis, KOL screening, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to gather structured public XiaoHongShu data for content research, competitor monitoring, comment analysis, creator tracking, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: XiaoHongShu search terms, URLs, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com service.

Mitigation: Use the skill only when that data sharing is acceptable, scope tokens appropriately, and rotate or revoke the token if exposure is suspected.

Risk: The skill may save local result logs containing collected public data or analysis inputs.

Mitigation: Review generated logs and delete them when they are no longer needed.

Risk: Using the tool for private, login-only, or unlawfully redistributed data could create compliance or privacy issues.

Mitigation: Limit use to public XiaoHongShu data and avoid private, hidden, login-only, or otherwise unauthorized content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-schedule-track)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [GUAIKEI API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; local result logs may be written during execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
