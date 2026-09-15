## Description:

Mautic (mautic.org). Use this skill for ANY Mautic request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Mautic contacts and segments through an OOMOL-connected account. It supports read operations plus confirmed create, update, delete, add-to-segment, and remove-from-segment actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that could execute local code if run without verification.

Mitigation: Install the oo CLI from a verified package or manually downloaded release with integrity checks, and do not allow an agent to run remote installer commands automatically.

Risk: Write and destructive actions can create, update, delete, or move Mautic contact data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Mautic Skill](https://clawhub.ai/oomol/skills/oo-mautic)
- [Mautic Homepage](https://mautic.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include live schema inspection steps and confirmation prompts for write or destructive Mautic actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
