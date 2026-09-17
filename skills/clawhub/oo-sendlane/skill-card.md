## Description:

Use this skill to operate Sendlane through an OOMOL-connected account for reading, creating, updating, and deleting campaigns, contact lists, tags, and custom fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sendlane marketing objects through the OOMOL oo CLI, including read operations and confirmed write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path uses a mutable remote installer for the oo CLI.

Mitigation: Review the official oo CLI source and use a verified installation path before installation.

Risk: Write and destructive actions can create, update, or delete Sendlane objects through the connected account.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Sendlane skill listing](https://clawhub.ai/oomol/skills/oo-sendlane)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Sendlane homepage](https://www.sendlane.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
