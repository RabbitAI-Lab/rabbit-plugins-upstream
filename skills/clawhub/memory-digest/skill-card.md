## Description:

Generate human-readable weekly/monthly reports from an AI agent's memory corpus by reading date-named daily memory logs and producing a digest with activity timeline, project momentum, open threads, and metric changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and individual users use this skill to turn an agent's date-named daily memory logs into weekly or monthly activity reports before planning, review, or scheduled reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local agent memory logs that may contain private or sensitive information.

Mitigation: Install and run it only where the operator is comfortable allowing local memory logs to be summarized, and review generated reports before sharing them.

Risk: Open threads, project momentum, and metrics are extracted heuristically and may include stale or already-resolved items.

Mitigation: Verify pending items and metrics before acting on them or presenting them as current status.

Risk: Cron usage can create recurring saved reports from memory logs.

Mitigation: Add scheduling only when recurring reports are intended, and choose an output location with appropriate access controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown digest by default, optional JSON report, and optional saved report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local memory logs; supports a configurable day window, output file path, and JSON mode.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
