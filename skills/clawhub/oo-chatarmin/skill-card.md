## Description:

Chatarmin lets an agent read, create, update, and delete Chatarmin data through the OOMOL oo CLI instead of calling the Chatarmin API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Chatarmin contacts, campaigns, flows, analytics, voucher pools, webhooks, and WhatsApp messages through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can involve running internet installer scripts for the oo CLI.

Mitigation: Prefer a verified package-manager or documented install path and review installer scripts before execution.

Risk: The connected Chatarmin account can create, update, delete, and send WhatsApp messages.

Mitigation: Require explicit user confirmation for write, destructive, webhook, voucher, or message-send actions and verify target identifiers and payloads.

## Reference(s):

- [Chatarmin homepage](https://chatarmin.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Chatarmin ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatarmin)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
