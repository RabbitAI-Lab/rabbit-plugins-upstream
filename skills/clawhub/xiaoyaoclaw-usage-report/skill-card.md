## Description:

Summarizes local OpenClaw session logs into task-duration, tool, skill, model, and token-usage reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators use this skill to inspect local agent activity, compare task and tool durations, and account for token use across agents and models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading session logs grants access to sensitive operational data.

Mitigation: Grant log-read access only when needed and treat resulting reports as sensitive.

Risk: A selected time window may expose more historical usage metadata than expected.

Mitigation: Verify or patch time-window filtering before relying on --today or --week as a privacy boundary.

Risk: Optional session details or full paths can reveal sensitive identifiers and local metadata.

Mitigation: Avoid --include-sessions and --include-paths unless necessary, and limit sharing of detailed output.

Risk: Scheduled reports can repeatedly disclose usage metadata.

Mitigation: Review the exact cron or HEARTBEAT schedule and payload before enabling automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-usage-report)
- [Usage documentation](https://github.com/dtsola/xiaoyaoclaw-usage-report)
- [Design notes](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Plain-text report or JSON, with an optional Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregated usage statistics by default; session details and full local paths require explicit opt-in. No cost estimates.]

## Skill Version(s):

1.0.6 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
