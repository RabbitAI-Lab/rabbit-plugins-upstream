## Description:

Guaikei XHS Explorer helps agents search public Xiaohongshu notes, retrieve note details and comments, and monitor creator posts through the Guaikei API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing analysts, brand operators, content creators, and agents use this skill to collect public Xiaohongshu search results, note details, comments, and creator posts for content research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install only when that data transfer is acceptable for the user's research context.

Risk: Retrieved public content and query context are saved locally by default.

Mitigation: Review or delete the generated logs directory when handling sensitive competitive research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-explorer)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI execution returns structured JSON and writes JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; retrieved public data and query context are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
