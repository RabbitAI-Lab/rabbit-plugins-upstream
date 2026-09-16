## Description:

Enables agents to read, create, update, and delete Paymo clients, projects, and tasks through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to manage Paymo clients, projects, tasks, and current-user lookups from an agent while relying on OOMOL-managed Paymo credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote oo CLI installer scripts.

Mitigation: Review the installer path before installing, and prefer a pinned, verified oo CLI release or official package source.

Risk: Paymo write and destructive actions can create, update, or delete client, project, and task data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or delete actions.

## Reference(s):

- [Paymo homepage](https://www.paymoapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Paymo skill release](https://clawhub.ai/oomol/skills/oo-paymo)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents are directed to inspect live connector schemas before sending JSON payloads and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
