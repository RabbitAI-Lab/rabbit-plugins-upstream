## Description:

Activates on every task to provide a six-phase workflow with traceability IDs, entry and exit gates, scope commitment, mandatory progress prints, and adaptive complexity handling for coding, documents, charts, data processing, planning, and questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured task workflow with phase gates, traceable scope decisions, verification checkpoints, and delivery reporting across coding and non-coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start a local background service and write runtime logs as part of ordinary activation.

Mitigation: Use it in an isolated development workspace, review the startup behavior, and disable or stop the local service when it is not needed.

Risk: The skill can use a stored GitHub PAT and alter global git identity and credential settings.

Mitigation: Provide credentials only when GitHub operations are required, prefer least-privilege temporary tokens, and inspect or reset global git configuration before sensitive work.

Risk: The skill can self-update, modify installed skill files, and keep persistent work records.

Mitigation: Review or disable self-update and persistent logging behavior before use in shared or sensitive repositories, and audit generated worklog and skill archive changes.

## Reference(s):

- [Stellar Trails ClawHub release](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [AskUserQuestion Gate Template](references/askuserquestion-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, file paths, workflow reports, and generated or modified artifacts when task scope requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task plans, phase reports, verification notes, worklog entries, local service commands, and repository changes depending on the user's request.]

## Skill Version(s):

9.11.6 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
