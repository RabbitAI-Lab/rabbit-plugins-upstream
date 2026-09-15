## Description:

Resource Flow (Hub Planner) lets agents use the OOMOL-connected oo CLI to read, create, and update Hub Planner projects and resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Hub Planner projects and resources through an OOMOL-connected account. It supports read operations and user-confirmed write actions such as creating projects or resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may run mutable remote installer scripts directly in a shell.

Mitigation: Review the installer source before execution and prefer official versioned installation instructions with checksum or signature verification.

Risk: Write actions such as create_project and create_resource can change Hub Planner account state.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

Risk: Connector use depends on the user's OOMOL account, Hub Planner connection, billing status, and server-side credentials.

Mitigation: Stop on authentication, connection, scope, or billing errors and ask the user to resolve the account issue before retrying.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-hub-planner)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Resource Flow (Hub Planner) Homepage](https://www.milientsoftware.com/hub-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
