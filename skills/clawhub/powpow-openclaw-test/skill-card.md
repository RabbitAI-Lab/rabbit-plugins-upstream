## Description:

Publishes travelogues or posts to PowPow and creates chat-capable digital humans pinned to the public map using the user's PowPow account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users use this skill through an OpenClaw-compatible agent to draft and publish travel posts, attach images and map locations, verify published content, and create digital humans on the PowPow public map.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide PowPow account passwords in chat.

Mitigation: Use it only with accounts appropriate for assistant-mediated publishing, and prefer an isolated or low-risk PowPow account.

Risk: A bearer session token is cached on disk without strong local protections.

Mitigation: Keep POWPOW_STATE_DIR in a private directory and clear the cached session when finished.

Risk: The skill can publish public content with location data.

Mitigation: Avoid sensitive photos, private places, and precise locations that should not appear on a public map.

Risk: Changing the configured platform URL can redirect account access or publishing behavior.

Mitigation: Do not change the platform URL unless the destination is trusted.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow map](https://global.powpow.online/map)
- [Security architecture](references/security.md)
- [File structure](references/file-structure.md)
- [Product screenshots](references/screenshots.md)
- [English source package](https://clawhub.ai/durenzidu/skills/powpow-simple-en)
- [Chinese source package](https://clawhub.ai/durenzidu/skills/powpow-simple)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and generated HTML post drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and a PowPow account; uses optional environment variables for state directory, password input, and image search.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter, ClawHub release metadata, changelog released 2026-09-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
