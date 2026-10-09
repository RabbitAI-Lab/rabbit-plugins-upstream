## Description:

Helps users turn a video, template, or original idea into short AI-generated videos and ad creatives with optional characters, product placement, and language choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use the skill to plan, price, generate, and deliver short-form videos or product ads through Riffkit, with user approval before paid actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation and heartbeat updates can replace local agent instructions with remote content without integrity checks.

Mitigation: Review the skill before installation, trust riffkit.ai for subsequent updates only if appropriate, or disable automatic updates and review each revision manually.

Risk: A locally stored Riffkit session grants account access if disclosed.

Mitigation: Protect ~/.riffkit/session as a credential; sign out and remove the session when access is no longer needed.

Risk: Generation, retries, billing actions, or uploads can spend credits or expose user content.

Mitigation: Confirm costs, uploads, retries, cancellations, and billing changes with the user before proceeding.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill release](https://clawhub.ai/riffkit/skills/riffkit)
- [API reference](https://riffkit.ai/skill/api.md)
- [Installation and updates](https://riffkit.ai/skill/install.md)
- [Creative direction guide](https://riffkit.ai/skill/anchor.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with video links and post captions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video links expire; videos remain in the user's Riffkit library.]

## Skill Version(s):

1.9.7 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
