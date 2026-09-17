## Description:

Mocean lets an agent operate Mocean account actions through the OOMOL oo connector, including balance checks, message status, pricing, phone number lookup, and SMS sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Mocean account and messaging workflows through an OOMOL-connected account. It is suited for reading account/service data and sending SMS only after the exact payload and effect are confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly in a shell.

Mitigation: Use a vetted installer path, inspect or verify the installer before execution where possible, and run installation with least privilege.

Risk: The send_sms action sends messages and may incur Mocean costs.

Mitigation: Confirm the exact SMS payload, recipient, and expected effect with the user before running send_sms.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-mocean)
- [Mocean Homepage](https://moceanapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before action execution; SMS sending changes state and can incur costs.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
