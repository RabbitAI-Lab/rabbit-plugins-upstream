## Description:

Riffkit helps agents create short AI videos and UGC-style ad creatives by analyzing a TikTok link, uploaded video, or saved template and adapting its attention formula to the user's product or creative direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan, submit, monitor, and deliver short-form AI video riffs or original ad videos. It is intended for workflows that turn one source, optional character or product settings, and a creative direction into post-ready video output with captions and hashtags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports a suspicious review-install posture because the heartbeat can replace local skill instructions from riffkit.ai after installation.

Mitigation: Use a manually reviewed, pinned version and do not enable heartbeat or force-update behavior unless the operator accepts remote instruction replacement.

Risk: The skill can submit paid video-generation work and failed retries may re-charge credits.

Mitigation: Require explicit pre-submit confirmation, surface 402 credit shortfalls without retrying, and state retry costs before resubmitting failed work.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)

## Skill Output:

**Output Type(s):** [guidance, API calls, markdown, shell commands]

**Output Format:** [Markdown guidance with API request details, shell commands, and returned video links or copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces user-facing plans, confirmation prompts, progress updates, finished video download links, captions, hashtags, and troubleshooting guidance.]

## Skill Version(s):

1.5.1 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
