## Description:

OpenClaw Usage Report helps agents parse local OpenClaw session JSONL files to summarize task duration, model and tool usage, skill usage, and token consumption without uploading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to ask an agent for local usage and performance summaries, including task duration, token usage by agent and model, tool latency, skill usage, session ranking, and daily trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local OpenClaw session logs to produce aggregate usage reports.

Mitigation: Install only when comfortable with local session-log analysis, and keep generated reports local unless they have been reviewed.

Risk: JSON exports may include cost fields and session-level metadata even though the main documentation emphasizes token-only reporting.

Mitigation: Review JSON exports before sharing them outside the local environment.

## Reference(s):

- [OpenClaw Usage Report on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-usage-report)
- [DESIGN.md](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with tables; optional JSON export and cron configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregated local OpenClaw session metrics; JSON export may include session-level metadata and cost fields when present.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
