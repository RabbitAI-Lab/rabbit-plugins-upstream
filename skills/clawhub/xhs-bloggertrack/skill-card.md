## Description:

xhs-bloggertrack helps agents retrieve public Xiaohongshu notes, note details, comments, and blogger post lists for content research, competitor analysis, KOL screening, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, and analysts use this skill to gather structured public Xiaohongshu data for content research, competitor monitoring, KOL screening, comment analysis, and trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Use the skill only when that data-sharing posture is acceptable, treat GUAIKEI_API_TOKEN as a secret, and avoid submitting sensitive business plans or private targets without approval.

Risk: Command results are written to a local logs directory and may include collected public comments, competitor targets, or campaign research.

Mitigation: Review and delete local logs when working on shared machines or after completing sensitive research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-bloggertrack)
- [Guaikei API access](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful command output includes status, request metadata, and result data.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
