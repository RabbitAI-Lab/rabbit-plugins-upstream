## Description:

Reports OpenClaw task duration, token usage, and tool, skill, and model activity from local session logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to review local task duration, token consumption, tool latency, and skill usage without sending session data to an external service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local session logs may contain sensitive information.

Mitigation: Share only the default aggregate report; enable session details or full paths only when needed and avoid sharing those outputs publicly.

Risk: Full-history reports or scheduled reports may expose more usage metadata than intended.

Mitigation: Keep the default today-only scope; use full-history and scheduled reporting only with explicit user approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-usage-report)
- [Usage documentation (linked in the skill)](https://github.com/dtsola/xiaoyaoclaw-usage-report)
- [Design and metric definitions](artifact/docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Text report or JSON statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregated, today-scoped statistics by default; session details, full paths, and full history require explicit options.]

## Skill Version(s):

1.0.7 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
