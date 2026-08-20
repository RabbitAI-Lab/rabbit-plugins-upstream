## Description:

Gupshup helps an agent list templates and send WhatsApp template or text messages through an OOMOL-connected Gupshup account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Gupshup account from an agent workflow, including listing message templates and sending approved WhatsApp template or text messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The send_template_message and send_text_message actions can send real WhatsApp messages through the connected Gupshup account.

Mitigation: Review the proposed action, recipient, message content, and payload with the user before running any write action.

Risk: Commands may fail when the oo CLI is unavailable or the connected account is not signed in, lacks scope, has expired credentials, or has insufficient credit.

Mitigation: Use the documented setup and reconnection steps only after the matching command failure occurs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gupshup)
- [Gupshup homepage](https://www.gupshup.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions should be reviewed with the user before execution.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
