## Description:

Searches public Xiaohongshu notes by keyword and retrieves note details, comments, and creator post lists for content research and creator monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and operators use this skill to collect public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and creator post tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu note links, profile links, and the GUAIKEI_API_TOKEN are sent to a third-party API.

Mitigation: Use the skill only for public Xiaohongshu data and only when the user is comfortable sending those inputs to guaikei.com.

Risk: Saved command results may persist on the local machine under logs/.

Mitigation: Clear the local logs directory periodically when saved query results should not remain on the machine.

Risk: Ambiguous social-media requests can lead to collecting the wrong public data set.

Mitigation: Confirm the Xiaohongshu platform, keyword, note URL, or profile URL before running a command when the request is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-track-creator-for-monitor)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON returned by the CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
