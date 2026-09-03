## Description:

Captures ticket resolution delays, misdiagnoses, escalation gaps, SLA breaches, knowledge gaps, and customer churn signals to support continuous support improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and agent developers use this skill to capture recurring support failures, SLA issues, knowledge base gaps, feature requests, and churn signals so they can be reviewed and promoted into support standards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can expose support context in repositories where Bash output may include secrets or customer data.

Mitigation: Enable hooks only per project, prefer the UserPromptSubmit reminder, narrow matchers to the support workflow, and avoid PostToolUse where command output may contain sensitive data.

Risk: Support learning logs may accidentally capture customer PII, account credentials, or internal authentication tokens.

Mitigation: Use ticket IDs and anonymized references, keep summaries short, and do not log PII, credentials, or auth tokens.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Examples](references/examples.md)
- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-support)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends support learning entries; hook reminders are optional and project-scoped.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
