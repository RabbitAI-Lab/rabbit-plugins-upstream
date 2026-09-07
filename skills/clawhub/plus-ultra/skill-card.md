## Description:

Run a Byzantine 2+1 plan before consequential work and a fresh, plan-blind reality check afterward.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Plus Ultra to require independent planning, explicit arbitration, and a fresh reality check before and after consequential changes. On Claude Code, the optional hook adapter can enforce recorded plan and verification steps when installed and tested; on other hosts it is a workflow convention unless separately integrated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional Claude Code setup installs broad persistent hooks that run a PATH-resolved command across sessions.

Mitigation: Install only when that persistent workflow gate is intended, pin the installer and repository version, use an absolute hook command path, and review hook settings before merging them.

Risk: Plan and reality verdict text can contain sensitive project details if users paste them into recorded verdicts.

Mitigation: Avoid putting secrets or private repository content in recorded verdict text.

Risk: The hook adapter is a workflow gate, not a sandbox or fail-closed authorization boundary.

Mitigation: Use operating-system permissions, isolated worktrees or containers, and credential boundaries for real enforcement.

## Reference(s):

- [Plus Ultra on ClawHub](https://clawhub.ai/antreasantoniou/skills/plus-ultra)
- [Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra)
- [Grade-A Pipeline](https://github.com/AntreasAntoniou/grade-a-pipeline)
- [Agent Collaboration Control](https://github.com/AntreasAntoniou/agent-collaboration-control)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Claude Code hook setup records plan and reality verdict text for the active session.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
