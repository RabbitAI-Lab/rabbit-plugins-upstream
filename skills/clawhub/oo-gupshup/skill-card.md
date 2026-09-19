## Description:

Operate Gupshup through an OOMOL-connected account by inspecting action schemas, listing message templates, and sending WhatsApp template or text messages with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Gupshup WhatsApp messaging through an OOMOL-connected account, including listing templates and sending approved template messages or text messages in active conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands for the oo CLI, which execute remote code on the user's machine.

Mitigation: Use an official, versioned oo CLI installer with checksum or signature verification, and run installer commands only after the user explicitly trusts the source.

Risk: Gupshup write actions can send WhatsApp messages through the connected account.

Mitigation: Confirm the exact action, recipient, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gupshup)
- [Gupshup homepage](https://www.gupshup.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that call Gupshup connector actions; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
