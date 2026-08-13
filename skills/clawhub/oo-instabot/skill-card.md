## Description:

Instabot helps agents inspect schemas and run Instabot user-management actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage Instabot users through their connected OOMOL account, including create, update, soft-delete, restore, get, and list workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or change Instabot user records.

Mitigation: Inspect the live action schema, review the exact payload with the user, and require explicit confirmation before running create or update actions.

Risk: Destructive actions can soft-delete Instabot users.

Mitigation: Confirm the specific target user and intended effect before deletion, and use the documented restore action when recovery is needed.

Risk: Auth, connection, or billing failures can interrupt connector execution.

Mitigation: Use first-time setup and recovery steps only after a command fails with the matching CLI, authentication, connection, scope, credential, or billing error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instabot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Instabot homepage](https://www.instabot.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions may run directly; write and destructive actions require explicit confirmation of the target and payload.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
