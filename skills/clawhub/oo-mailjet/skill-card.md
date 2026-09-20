## Description:

Mailjet (mailjet.com). Use this skill for ANY Mailjet request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Mailjet contacts through an OOMOL-connected account, including creating, retrieving, listing, and updating contacts while confirming state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed automatically.

Mitigation: Review installer instructions before installation and use a safer reviewed installation channel or manually verify the installer before executing it.

Risk: Write actions can change Mailjet contact state.

Mitigation: Confirm the exact payload and expected effect with the user before running create_contact or update_contact.

## Reference(s):

- [Mailjet homepage](https://www.mailjet.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Mailjet skill on ClawHub](https://clawhub.ai/oomol/skills/oo-mailjet)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests and requires confirmation for write actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
