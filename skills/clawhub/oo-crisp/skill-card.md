## Description:

Crisp (crisp.chat). Use this skill for ANY Crisp request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, developers, and support operators use this skill to work with Crisp conversations through an OOMOL-connected account, including retrieving website and conversation data and sending confirmed operator text messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute an unverified remote installer with the user's privileges.

Mitigation: Review the installer path before installing, and prefer a trusted package manager or downloaded verified release for the oo CLI when available.

Risk: The message-sending action can post operator text to Crisp conversations through the connected account.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-crisp)
- [Crisp Homepage](https://crisp.chat/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON connector responses.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
