## Description:

Publishes travel posts to PowPow and creates public digital humans pinned to the PowPow map, using the user's PowPow account for login, drafting, image handling, geocoding, publishing, verification, deletion of the user's own posts, and digital-human creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users use this skill to turn travel photos or notes into posts on PowPow, or to create a digital human that can chat and appear on the public map. It is intended for user-directed publishing workflows where the user supplies account access and confirms content before public posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to handle PowPow login and stores a reusable local session token.

Mitigation: Use only with a PowPow account you intend the agent to access, keep the session directory private, and delete ~/.powpow/session.json after use.

Risk: Posts, uploaded images, and selected locations can become public on the PowPow map.

Mitigation: Review drafts and location choices before publishing, and do not provide sensitive images or locations unless they are intended to be public.

Risk: Scripts can publish, delete the user's own posts, or create public digital humans without their own confirmation gate.

Mitigation: Require explicit user confirmation before running publish, delete, or digital-human creation steps.

Risk: Digital-human creation can spend PowPow badges.

Mitigation: Confirm the badge cost and public 30-day digital-human behavior before creation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-simple-vi)
- [Publisher profile](https://clawhub.ai/user/durenzidu)
- [PowPow homepage](https://global.powpow.online)
- [Artifact README](artifact/README.md)
- [Security reference](artifact/references/security.md)
- [Screenshots reference](artifact/references/screenshots.md)
- [File structure reference](artifact/references/file-structure.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversation guidance with inline shell commands and generated post draft content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public PowPow posts, uploaded images, map locations, or public digital humans when the user authorizes those actions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
