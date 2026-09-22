## Description:

Riff winning short videos from one source, such as a TikTok link, uploaded video, analyzed template, or written creative direction, into post-ready AI video or UGC-style ad creative with optional character, product placement, and language settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to plan, submit, monitor, and deliver short-form AI video riffs or ad creatives from a source video, template, product, or creative direction. It helps the agent gather required inputs, require confirmation before paid generation actions, and return finished video links with captions, hashtags, and strategy recaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat can replace local skill instructions from riffkit.ai after installation.

Mitigation: Enable the heartbeat only if riffkit.ai is trusted, or disable auto-update and pin reviewed skill versions.

Risk: The skill can guide uploads, video generation, retries, and subscription-related actions that may affect the user's account or balance.

Mitigation: Require explicit user confirmation before uploads, generation, retries, and subscription changes, and review the planned source, product, character, language, and creative direction before submission.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit publisher profile](https://clawhub.ai/user/riffkit)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, API calls, Shell commands]

**Output Format:** [Markdown guidance with API request details, shell commands for setup or heartbeat checks, generated video links, captions, hashtags, and strategy recaps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid generation, retry, upload, or account-affecting actions.]

## Skill Version(s):

1.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
