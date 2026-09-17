## Description:

Agiled (agiled.app). Use this skill for ANY Agiled request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Agiled through an OOMOL-connected account, including listing, reading, creating, updating, and deleting contacts, projects, and tasks. It is intended for Agiled workflows where the agent should inspect the live action schema before sending an oo CLI request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the OOMOL CLI installation path before installation; prefer a pinned, verifiable installer or official package-manager method and do not run curl-to-bash or irm-to-iex commands automatically.

Risk: Write and destructive Agiled actions can change or remove CRM, project, and task data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Agiled homepage](https://agiled.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Agiled skill page](https://clawhub.ai/oomol/skills/oo-agiled)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action-schema inspection before constructing request payloads; read actions can run directly, while write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
