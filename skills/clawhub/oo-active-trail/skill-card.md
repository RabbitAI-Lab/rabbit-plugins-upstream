## Description:

ActiveTrail connector for reading, creating, updating, and deleting ActiveTrail contacts, groups, memberships, and account balance data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ActiveTrail through an OOMOL-connected account, including contact and group management, group membership changes, and account balance lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer source before execution, prefer a verified package or documented installer with checksum or signature validation, and avoid running the installer from an elevated shell.

Risk: Write and destructive ActiveTrail actions can change or remove contacts, groups, and memberships.

Mitigation: Fetch the live action schema, confirm the exact target and payload with the user, and require explicit approval before running write or destructive actions.

## Reference(s):

- [ActiveTrail homepage](https://www.activetrail.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-active-trail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke ActiveTrail read, write, and destructive connector actions after schema inspection and user confirmation where needed.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
