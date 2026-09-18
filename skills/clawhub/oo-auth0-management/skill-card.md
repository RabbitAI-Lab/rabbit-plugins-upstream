## Description:

Auth0 Management helps agents operate Auth0 Management through the OOMOL auth0_management connector and oo CLI for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and identity administrators use this skill to inspect Auth0 Management action schemas and run read, write, and destructive Auth0 role, permission, and user-management actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes shell and PowerShell commands that run remote installer scripts.

Mitigation: Review the setup path before installing, prefer a signed or package-manager installation for the oo CLI, verify release integrity where possible, and do not allow an agent to run the remote installer automatically.

Risk: Auth0 role and permission actions can change or remove access controls.

Mitigation: Confirm Auth0 scopes carefully and require explicit approval for role or permission changes, especially actions tagged write or destructive.

## Reference(s):

- [Auth0 Management homepage](https://auth0.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-auth0-management)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
