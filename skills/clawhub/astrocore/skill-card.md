## Description:

Connects an agent to the owner's AstroCore workspace for chat, memory, reports, gallery items, and voice replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dimasash2005-ship-it](https://clawhub.ai/user/dimasash2005-ship-it)

### License/Terms of Use:

MIT-0

## Use Case:

Owners use this skill to connect their agent to AstroCore and ask it to read or save approved memory, reports, and gallery items, or respond through AstroCore chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AstroCore API key grants access to the owner's workspace data.

Mitigation: Keep the key secret and revoke it if exposed.

Risk: Selected memory, reports, gallery metadata, and chat media paths are shared with AstroCore.

Mitigation: Share only owner-approved content; exclude passwords, card numbers, and unrelated private data.

## Reference(s):

- [AstroCore](https://astrocore.one)
- [AstroCore skill on ClawHub](https://clawhub.ai/dimasash2005-ship-it/skills/astrocore)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown, with optional shell commands or a voice-reply media path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and gallery items can be saved to the owner's AstroCore workspace.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
