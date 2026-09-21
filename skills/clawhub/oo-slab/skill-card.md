## Description:

Provides Slab access through the OOMOL oo CLI for reading, creating, updating, deleting, and searching Slab content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a connected Slab workspace through the OOMOL oo CLI, including organization lookup, content search, post and topic reads, and confirmed write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may guide an agent to run remote installer scripts with broad local execution authority.

Mitigation: Prefer installing the oo CLI from trusted documentation, verify the source where possible, and require explicit user approval before running remote installer commands.

Risk: Write and destructive Slab actions can change or remove workspace content.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: Authentication, connection, scope, and billing failures can interrupt Slab operations.

Mitigation: Use first-time setup steps only after a matching failure and direct the user to sign in, reconnect Slab, refresh scopes, or resolve billing before retrying.

## Reference(s):

- [ClawHub Slab skill page](https://clawhub.ai/oomol/skills/oo-slab)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Slab homepage](https://slab.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
