## Description:

Sage Sales Management (forcemanager.com). Use this skill for ANY Sage Sales Management request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect schemas and manage Sage Sales Management accounts, contacts, and opportunities through an OOMOL-connected account. It supports read, list, create, update, and delete workflows with explicit confirmation expected before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI, which can execute unverified code on the user's machine.

Mitigation: Review the installer source and prefer a signed or package-manager-based installation path before using the skill.

Risk: Create, update, and delete actions can change or remove Sage Sales Management CRM records.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [Sage Sales Management homepage](https://www.forcemanager.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sage-sales-management)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
