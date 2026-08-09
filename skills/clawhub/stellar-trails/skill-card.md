## Description:

Stellar Trails provides an always-on six-phase workflow for coding, document creation, visualization, data processing, planning, and question-answering tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured workflow with specification, planning, implementation, verification, and delivery gates across common work requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs on nearly every task and can materially change the agent's default interaction pattern.

Mitigation: Install it only when an always-on workflow framework is desired, and review activation and phase-gate behavior before deployment.

Risk: The skill can start a persistent preview server.

Mitigation: Disable or restrict persistent server startup unless it is needed and acceptable in the target environment.

Risk: The skill includes self-update behavior and local file synchronization.

Mitigation: Remove or disable forced self-update behavior before installation unless automatic updates are intentionally approved.

Risk: The skill can configure GitHub credentials from a PAT.

Mitigation: Remove or disable automatic PAT handling before installation, and manage credentials through approved secret-handling procedures.

Risk: The skill can retain local logs, memory, and profile data across sessions.

Mitigation: Disable persistent profile and worklog retention where cross-session data storage is not required or permitted.

## Reference(s):

- [Stellar Trails ClawHub Release](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Workflow Phases](artifact/procedure/phases.md)
- [AskUserQuestion Gate Template](artifact/references/askuserquestion-gate.md)
- [Architecture](artifact/knowledge/architecture.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown instructions with inline shell commands, checklists, and delivery reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow traces, phase markers, risk notes, and task-specific guidance for the active agent session.]

## Skill Version(s):

9.11.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
