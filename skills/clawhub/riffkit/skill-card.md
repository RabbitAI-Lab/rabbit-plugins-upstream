## Description:

Riffkit turns one source video or analyzed template into a post-ready short-form AI video or UGC-style ad creative, with optional digital character, product placement, language, and creative direction settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and agents use this skill to plan and submit short-form video riffs from a TikTok link, uploaded video, analyzed template, or written creative direction, then monitor the job and return finished video assets with captions and hashtags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat or force-update path can replace the installed skill instructions from a remote URL without verification.

Mitigation: Keep automatic updates disabled unless releases are verified out of band, and manually review downloaded updates before replacing SKILL.md.

Risk: The skill can perform Riffkit API access and chargeable video-generation actions after user confirmation.

Mitigation: Require explicit confirmation before submission, avoid automatic retries, and surface insufficient-credit responses without retrying or silently continuing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill definition](https://riffkit.ai/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, API calls, Shell commands, Configuration]

**Output Format:** [Markdown and plain text with API request guidance and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return video download links, captions, hashtags, task status summaries, and update-check instructions.]

## Skill Version(s):

1.5.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
