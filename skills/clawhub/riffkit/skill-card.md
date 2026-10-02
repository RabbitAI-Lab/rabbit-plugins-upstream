## Description:

Helps agents turn a source video, template, or written creative direction into short AI-generated videos and ad creatives with optional characters, products, and language choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and other external users can ask an agent to adapt a video's creative formula, swap elements into its shots, or create an original short-form ad, then retrieve the resulting video and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable account session is stored on disk.

Mitigation: Restrict access to the session file, avoid sharing it, and remove the stored session when no longer needed.

Risk: The automatic heartbeat can replace the local skill definition with content from riffkit.ai.

Mitigation: Disable automatic updates or review the downloaded skill definition before allowing it to overwrite the local copy.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill definition](https://riffkit.ai/SKILL.md)
- [Riffkit heartbeat and update procedure](https://riffkit.ai/HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Markdown]

**Output Format:** [Text or Markdown with generated-video links, captions, and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a Riffkit account and user confirmation before paid submission.]

## Skill Version(s):

1.8.17 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
