## Description:

This skill enables agents to read, create, update, and delete MaintainX data through an OOMOL-connected MaintainX account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting maintenance operations use this skill to list and retrieve MaintainX locations, users, work orders, and comments, and to create, update, or delete approved records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and irm-to-iex installer commands for the oo CLI.

Mitigation: Prefer an official, versioned, verifiable installation method and avoid running remote installer scripts blindly.

Risk: The skill can run write and destructive MaintainX actions through a connected account.

Mitigation: Confirm the exact payload, target record, and expected effect with the user before running write or delete actions.

Risk: Connector access depends on the user's OOMOL account, MaintainX connection, scopes, credentials, and billing state.

Mitigation: Run setup or connection steps only after a command fails with a matching authentication, scope, credential, app, or billing error.

## Reference(s):

- [MaintainX Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-maintainx)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MaintainX Homepage](https://www.getmaintainx.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
