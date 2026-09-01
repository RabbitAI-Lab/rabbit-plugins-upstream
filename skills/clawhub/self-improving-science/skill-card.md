## Description:

Captures reusable research learnings, experiment issues, feature requests, and methodology corrections for scientific research and ML workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and ML practitioners use this skill to record data quality issues, reproducibility failures, statistical corrections, hypothesis revisions, and research tooling requests as durable markdown notes. It can also provide project-scoped reminders and help turn reviewed recurring learnings into reusable skill scaffolds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable research-learning notes can capture sensitive project, dataset, patient, or credential details if used carelessly.

Mitigation: Redact sensitive data before logging, avoid raw data samples and secrets, and prefer summary statistics or redacted excerpts.

Risk: Persistent hooks can add reminders across future sessions if enabled too broadly.

Mitigation: Keep hooks project-scoped, use narrow matchers, and prefer the activator-only hook unless error-pattern reminders are needed.

Risk: Promotion into agent memory, hook files, or generated skills can change future agent behavior.

Mitigation: Require a reviewed diff and explicit user approval before writing to AGENTS.md, TOOLS.md, SOUL.md, MEMORY.md, hook files, or generated skills.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, hook configuration snippets, and structured markdown log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends .learnings markdown entries; optional hooks emit reminder text; extraction helper can scaffold skill markdown after review.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
