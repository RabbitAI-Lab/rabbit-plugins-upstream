## Description:

Chatarmin lets an agent operate Chatarmin through an OOMOL-connected account for reading, creating, updating, deleting, and sending WhatsApp messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Chatarmin contacts, campaigns, flows, voucher pools, webhooks, analytics, and WhatsApp messaging through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified internet installer commands in the setup path could execute arbitrary local code.

Mitigation: Review the setup path before installing and prefer a trusted, verifiable OOMOL CLI package or an installer that can be inspected and verified.

Risk: Write, delete, webhook, voucher, or message actions can change Chatarmin state or send messages.

Mitigation: Confirm the exact target and payload before running state-changing or destructive actions.

## Reference(s):

- [Chatarmin homepage](https://chatarmin.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON data and execution identifiers from Chatarmin actions.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
