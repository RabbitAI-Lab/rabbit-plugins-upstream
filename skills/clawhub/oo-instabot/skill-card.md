## Description:

Instabot (instabot.io). Use this skill for ANY Instabot request: reading, creating, updating, and deleting data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Instabot users through an OOMOL-connected account, including reading user data and performing confirmed create, update, soft-delete, and restore actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes download-and-run installer commands for the oo CLI.

Mitigation: Review the installation source before use and prefer an official, versioned installer with checksum or signature verification.

Risk: Create, update, delete, and restore actions can change Instabot state.

Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instabot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Instabot homepage](https://www.instabot.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke live oo CLI connector schema and run commands that return JSON responses.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
