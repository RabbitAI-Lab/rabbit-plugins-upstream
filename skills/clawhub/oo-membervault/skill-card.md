## Description:

Use this skill for MemberVault requests through an OOMOL-connected account, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate MemberVault through the OOMOL `oo` CLI, including inspecting live action schemas, adding users, listing products or courses, removing product access, and deleting users after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that are not pinned or integrity-checked.

Mitigation: Review or replace remote installer commands with a verified vendor installation path before installation.

Risk: Write and destructive actions can add users, remove product access, or permanently delete MemberVault users and their data.

Mitigation: Require explicit user confirmation of the action, target, payload, and expected effect before running `add_user`, `remove_user`, or `delete_user`.

Risk: Credentialed actions could affect the wrong OOMOL or MemberVault account if the active connection is not the intended one.

Mitigation: Use the skill only with the intended OOMOL and MemberVault account and verify connection errors before reconnecting.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-membervault)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MemberVault Homepage](https://membervault.co/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce `oo connector schema` and `oo connector run` commands whose JSON responses include connector data and an execution id.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
