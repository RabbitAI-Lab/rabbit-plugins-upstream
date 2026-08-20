## Description:

Riffkit helps agents turn a TikTok link, uploaded video, analyzed template, or written creative direction into short AI videos and UGC-style ad creatives with optional character, product placement, and language controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan, submit, monitor, and retrieve short AI video generations for riff videos or original ad creatives. It supports source selection, optional creative direction, product and character settings, authenticated API calls, billing-aware handling, and delivery of finished video links with copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an authenticated account session to create and manage video-generation resources.

Mitigation: Use the documented device authorization flow, keep the session token out of prompts and generated content, and confirm paid generation or retry actions before calling generation endpoints.

Risk: The optional heartbeat can replace the local skill definition from a remote Riffkit URL.

Mitigation: Disable automatic heartbeat updates or route updates through a reviewed marketplace or manual install flow when change control is required.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)
- [Riffkit heartbeat procedure](https://riffkit.ai/HEARTBEAT.md)
- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit publisher profile](https://clawhub.ai/user/riffkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and API request details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing plans, confirmations, progress summaries, finished video links, captions, hashtags, and operational guidance; it does not itself publish generated videos to social platforms.]

## Skill Version(s):

1.3.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
