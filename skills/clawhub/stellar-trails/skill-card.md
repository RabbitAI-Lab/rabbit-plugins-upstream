## Description:

Activates on every task: coding, documents, charts and visualizations, data processing, multi-step planning, or simple questions, using a six-phase workflow with traceability IDs, entry and exit gates, scope commitment, and enforcement layers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to structure coding, document, data, visualization, planning, and troubleshooting work through a gated task workflow with visible activation and delivery reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic activation can perform sensitive setup and persistent background activity, including local credential use, global Git configuration changes, local web server startup, self-update behavior, and cross-session state storage.

Mitigation: Install and run the skill only in an isolated environment where those behaviors are acceptable; disable or remove automatic activation side effects before using it near sensitive repositories, credentials, or private task data.

Risk: Persistent local logs and task/profile data may retain operational context across sessions.

Mitigation: Review stored state before and after use, avoid entering private task data unless persistence is acceptable, and clear the skill's persistent data when the session no longer needs it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [AskUserQuestion gate reference](references/askuserquestion-gate.md)
- [z.ai sandbox notes](knowledge/zai-sandbox.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline code or shell commands when task work requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow banners, phase markers, scope summaries, verification notes, and delivery reports.]

## Skill Version(s):

9.11.5 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
