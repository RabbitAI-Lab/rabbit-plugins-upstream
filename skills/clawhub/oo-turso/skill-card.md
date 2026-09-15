## Description:

Turso (turso.tech). Use this skill for ANY Turso request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Turso connector schemas, run Turso database and organization actions through the OOMOL-connected oo CLI, and manage database or group lifecycle tasks with confirmation for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may run unverified code in a shell.

Mitigation: Prefer a pinned, verifiable oo CLI release or trusted package manager, and do not run installer commands from an elevated shell.

Risk: Create and delete actions can change or remove Turso resources.

Mitigation: Confirm the exact action, target, payload, and expected effect before running write or destructive operations.

## Reference(s):

- [Turso homepage](https://turso.tech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-turso)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
