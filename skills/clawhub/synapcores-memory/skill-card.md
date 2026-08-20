## Description:

Give the agent long-term memory that survives restarts — store facts, recall them semantically, and forget them on request — backed by a self-hosted SynapCores database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synapcores](https://clawhub.ai/user/synapcores)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill when an agent should remember user-approved facts across sessions, recall them semantically, correct or delete stored facts, and keep memory in a self-hosted SynapCores database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remembered facts persist across sessions in the user's SynapCores database.

Mitigation: Store only user-approved, self-contained facts, use separate namespaces for people or projects, and use the documented hard-delete flow when the user asks to forget something.

Risk: Sensitive personal details or credentials could be intentionally stored if the agent applies the memory workflow too broadly.

Mitigation: Ask for confirmation before saving sensitive personal details and never store credentials, payment details, or regulated data.

Risk: The companion plugin advertises automatic capture behavior that differs from this manual skill.

Mitigation: Review the companion plugin separately before installing it and confirm which SynapCores memory backend is active.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/synapcores/skills/synapcores-memory)
- [Project homepage](https://github.com/SynapCores/synapcores-openclaw-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, jq, and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running SynapCores gateway plus curl, jq, SYNAPCORES_API_KEY, and optionally SYNAPCORES_URL.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
