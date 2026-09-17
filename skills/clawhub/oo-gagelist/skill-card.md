## Description:

GageList connector skill for reading, creating, updating, and deleting data in a connected GageList account through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate GageList through an OOMOL-connected account, including retrieving gage and calibration records and managing manufacturer records. Actions that change or delete GageList data require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags remote pipe-to-shell installer guidance as requiring review before installation.

Mitigation: Install the oo CLI through a verified, user-controlled method and do not let an agent run remote installer scripts automatically.

Risk: The skill can create, update, and delete manufacturer records in the connected GageList account.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write or destructive action.

Risk: Using the connector grants an agent access to a connected GageList account through OOMOL-managed credentials.

Mitigation: Use the skill only when the user trusts OOMOL and intends to grant connector access to that account.

## Reference(s):

- [ClawHub GageList skill page](https://clawhub.ai/oomol/skills/oo-gagelist)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [GageList homepage](https://gagelist.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
