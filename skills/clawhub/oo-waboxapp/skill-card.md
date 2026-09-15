## Description:

waboxapp helps agents operate Waboxapp through an OOMOL-connected account using the oo CLI to check account status and send WhatsApp chats, images, links, and media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Waboxapp from an agent through their connected OOMOL account, including checking account status and sending WhatsApp text, image, link, and media messages after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer commands that can execute arbitrary code.

Mitigation: Review the installer source and prefer a signed or checksum-verified oo CLI installation path before using first-time setup.

Risk: send_chat, send_image, send_link, and send_media affect the connected WhatsApp account.

Mitigation: Confirm the exact recipient, payload, and effect with the user before allowing any account-affecting send action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waboxapp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [waboxapp homepage](https://www.waboxapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI and live connector schemas; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
