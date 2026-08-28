## Description:

Parse, filter, and summarize standard text, JSON, and delimited logs for errors, warnings, recurring patterns, and time-based anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to triage production issues, audit system behavior, and extract actionable signals from local log files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local logs can contain secrets, user data, IP addresses, and operational details.

Mitigation: Use the skill only on intended log paths, avoid sharing sensitive excerpts, and review commands before running them in sensitive environments.

Risk: Command examples may produce incomplete or misleading summaries if log formats, timestamps, or filters do not match the target files.

Mitigation: Review generated commands and validate findings against the raw logs before acting on triage conclusions.

## Reference(s):

- [ClawHub skill page: log-analyzer](https://clawhub.ai/terrycarter1985/skills/log-analyzer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only log-analysis guidance using standard Unix tools; JSON log examples use jq.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
