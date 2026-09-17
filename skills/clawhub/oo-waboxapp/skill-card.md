## Description:

waboxapp connector skill that lets an agent inspect waboxapp action schemas, check account status, and send WhatsApp chats, images, links, and media through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate waboxapp through an OOMOL-connected account, including checking account status and sending WhatsApp messages or media after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes piping a remote installer script into a shell.

Mitigation: Install the oo CLI from a verified release or package manager when possible, or review the installer before execution.

Risk: waboxapp write actions can send WhatsApp chats, images, links, or media to external recipients.

Mitigation: Review and confirm the exact outgoing payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waboxapp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [waboxapp homepage](https://www.waboxapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect schemas or run waboxapp connector actions; write actions require user confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
