## Description:

Captures data quality issues, metric drift, pipeline failures, misleading visualizations, metric definition mismatches, and data freshness problems to enable continuous analytics improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, analytics engineers, and BI teams use this skill to capture recurring analytics issues and convert proven patterns into data dictionaries, pipeline runbooks, dashboard standards, and data quality SLAs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks can add reminders to future agent sessions beyond the immediate task.

Mitigation: Keep hooks project-scoped and use the prompt reminder path unless Bash-output detection is specifically needed.

Risk: Analytics learnings may accidentally include secrets, PII, or sensitive query output.

Mitigation: Redact credentials, PII, raw query results, and full table dumps before writing learning entries.

Risk: Promoting entries into AGENTS.md, TOOLS.md, MEMORY.md, hooks, or generated skills can change future agent behavior.

Mitigation: Review proposed changes and apply promotions only after explicit user approval.

## Reference(s):

- [Self-Improving Analytics ClawHub Page](https://clawhub.ai/jose-compu/skills/self-improving-analytics)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured log-entry templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local learning logs only when the agent follows the skill workflow; optional hooks emit reminder text.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
