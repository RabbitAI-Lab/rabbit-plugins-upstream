## Description:

Auth0 Management helps agents read, create, update, and delete Auth0 Management data through the OOMOL auth0_management connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Auth0 users, roles, and permissions through schema-inspected OOMOL connector actions while confirming write and destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can ask an agent to run remote installer scripts without independent verification.

Mitigation: Review and verify the OOMOL CLI installer source before running remote install commands.

Risk: Auth0 write and destructive actions can change roles, permissions, or user assignments.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-auth0-management)
- [Auth0 Management Homepage](https://auth0.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
