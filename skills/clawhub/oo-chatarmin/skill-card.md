## Description:

Chatarmin (chatarmin.com). Use this skill for ANY Chatarmin request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Chatarmin contacts, campaigns, flows, voucher pools, webhooks, and WhatsApp message sending through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may install the oo CLI by piping a remote installer directly into a shell.

Mitigation: Install the oo CLI from a trusted OOMOL source yourself and verify the installer where possible before allowing the skill to use it.

Risk: Write, delete, webhook, voucher, and message-sending actions can change Chatarmin state or send WhatsApp messages.

Mitigation: Require explicit approval for the exact target, payload, and expected effect before running state-changing or destructive actions.

## Reference(s):

- [ClawHub Chatarmin Skill Page](https://clawhub.ai/oomol/skills/oo-chatarmin)
- [Chatarmin Homepage](https://chatarmin.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL authentication, and a connected Chatarmin account.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
