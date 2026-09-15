## Description:

Operate Gupshup through an OOMOL-connected account for reading, creating, and updating Gupshup data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list Gupshup message templates and send WhatsApp template or text messages through an OOMOL-connected Gupshup account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote oo CLI installer scripts directly in a shell without verification.

Mitigation: Download, inspect, pin, and verify the installer or binary before installation.

Risk: Write actions can send WhatsApp messages through the connected Gupshup app.

Mitigation: Review the exact recipient, message content, payload, and intended effect before approving any send action.

## Reference(s):

- [ClawHub Gupshup skill page](https://clawhub.ai/oomol/skills/oo-gupshup)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gupshup homepage](https://www.gupshup.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
