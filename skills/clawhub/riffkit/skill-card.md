## Description:

Helps create short AI videos and ad creatives from a source video, template, or original creative direction, with optional characters, product placement, and language choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn a source video or original concept into short-form videos and UGC-style ads, then receive a video link and post text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable login session is stored on disk and can grant account access if exposed.

Mitigation: Protect the session file, never paste credentials into chat, and sign out if a credential is exposed.

Risk: An enabled heartbeat can replace local skill instructions with remote files without separate review.

Mitigation: Disable automatic updates or review each new skill version before allowing it to change agent behavior.

Risk: Selected media is uploaded to Riffkit and video creation can spend credits.

Mitigation: Confirm the media is intended for upload, and approve the quoted price and plan before spending credits or retrying a chargeable task.

## Reference(s):

- [Riffkit ClawHub listing](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill instructions](https://riffkit.ai/SKILL.md)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)
- [Riffkit installation guide](https://riffkit.ai/skill/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with video links, post text, and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a link to a completed video rather than a local video file.]

## Skill Version(s):

1.10.2 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
