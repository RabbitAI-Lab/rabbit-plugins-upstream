## Description:

Helps creators turn a source video or creative brief into an original short AI video or ad, with optional characters, product placement, and language selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to plan, generate, and deliver short-form AI videos and product ads from a source video or creative direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic updates can replace the skill's instructions with content from riffkit.ai.

Mitigation: Disable the heartbeat or review downloaded instructions before accepting updates.

Risk: Agent access to a Riffkit account exposes a reusable login session.

Mitigation: Grant access only when needed and protect or remove ~/.riffkit/session afterward.

Risk: Video generation and related actions can spend account credits.

Mitigation: Review the quoted price and plan, including retries or extra formats, before approving each charge.

## Reference(s):

- [Riffkit on ClawHub](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit website](https://riffkit.ai)
- [Riffkit skill documentation](https://riffkit.ai/SKILL.md)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)
- [Riffkit installation and updates](https://riffkit.ai/skill/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with quoted plans, commands, and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed videos are shared through time-limited links; generation may spend account credits after approval.]

## Skill Version(s):

1.10.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
