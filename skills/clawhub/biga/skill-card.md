## Description:

BigA helps agents analyze China A-share stocks by combining real-time quotes, quantitative scoring, technical timing, fundamental screening, stock-pool monitoring, and buy/sell signal summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use BigA to monitor A-share stock pools, screen candidate stocks, summarize market context, and produce timed stock-analysis messages with long-term and short-term action guidance. The skill is intended for informational stock analysis and includes recurring morning, intraday, and closing-review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send automated financial recommendations that may be inaccurate, incomplete, or unsuitable for a user's circumstances.

Mitigation: Treat all signals as unverified informational analysis, independently review source data and assumptions, and avoid making trading decisions from the skill output alone.

Risk: The skill can create recurring weekday jobs that send stock-analysis messages to configured channels.

Mitigation: Review cron schedules, target channels, and recipients after installation, and disable scheduled delivery until the user explicitly wants recurring messages.

Risk: The release guidance flags an unpinned DSH plugin path and data-source or timing-score issues.

Mitigation: Avoid or separately verify the DSH plugin path, and prefer disabling scheduled delivery until data-source and timing-score behavior has been reviewed.

## Reference(s):

- [BigA ClawHub Skill Page](https://clawhub.ai/kobenfang/skills/biga)
- [Technical Timing Score Framework](references/technical-timing-score.md)
- [User Preferences Reference](references/user-preferences.md)
- [Sector Matrix Reference](references/sector-matrix.md)
- [Cron Templates](references/cron-templates.json)
- [Cron Install Shell Template](references/cron-install-shell.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown/text stock-analysis summaries, JSON scan output, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Segmented stock-analysis messages may be split for channel delivery; financial signals are informational and not investment advice.]

## Skill Version(s):

6.0.21 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
