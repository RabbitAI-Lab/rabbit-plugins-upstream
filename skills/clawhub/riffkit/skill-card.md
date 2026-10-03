## Description:

Creates short AI videos and ad creatives by adapting a source video's emotional formula, swapping elements in its shots, or following an original creative brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use Riffkit to turn a video reference or written brief into short-form videos and product ads, with optional characters, product placement, and language settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scheduled heartbeat can replace the reviewed skill definition with a new version from riffkit.ai.

Mitigation: Disable automatic updates or require signed or manually reviewed updates before use.

Risk: The skill saves a local session cookie and sends authenticated requests to Riffkit.

Mitigation: Restrict access to the session file, review API traffic, and remove the saved session when no longer needed.

Risk: Video submissions and retries can consume paid credits.

Mitigation: Require explicit user confirmation before each paid action.

## Reference(s):

- [Riffkit website](https://riffkit.ai)
- [Riffkit on ClawHub](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit heartbeat instructions](https://riffkit.ai/HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Video links]

**Output Format:** [Markdown response with video download link, caption, and hashtags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos require an authenticated session to download.]

## Skill Version(s):

1.8.22 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
