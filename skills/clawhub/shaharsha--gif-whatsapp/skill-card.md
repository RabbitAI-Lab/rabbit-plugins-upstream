## Description:

Search and send GIFs on WhatsApp. Handles the Tenor→MP4 conversion required for WhatsApp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shaharsha](https://clawhub.ai/user/shaharsha)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find reaction GIFs, convert them into WhatsApp-compatible MP4 media, and send them through the platform message tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send WhatsApp media and uses broad command execution for media handling.

Mitigation: Install and invoke it only when the agent is expected to send GIFs, and review the selected recipient and media before sending.

Risk: The workflow processes downloaded remote GIF files with local media-conversion commands.

Mitigation: Use trusted GIF-provider results, give temporary files unique names, and delete generated media after delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shaharsha/skills/gif-whatsapp)
- [Publisher profile](https://clawhub.ai/user/shaharsha)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces temporary GIF and MP4 media files for WhatsApp delivery.]

## Skill Version(s):

1.3.0 (source: server release metadata; artifact frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
