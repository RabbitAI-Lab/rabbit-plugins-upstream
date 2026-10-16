## Description:

Transcribes and translates video speech, burns translated subtitles into a video, and optionally adds a timing-aligned dubbed track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to translate spoken video into subtitles and, when requested, produce a dubbed video aligned with the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is uploaded to dLazy cloud services for processing.

Mitigation: Confirm the video is appropriate to share with dLazy before uploading private material.

Risk: Installing and running an external CLI executes third-party code locally.

Mitigation: Prefer the version-pinned npx invocation or review the CLI source before installing it globally.

Risk: Transcription, translation, and per-cue dubbing calls consume paid credits.

Mitigation: Confirm the target language and expected cost before processing large videos; use dry-run where available.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source code (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Burned-in translated subtitles; an aligned dubbed audio track only when requested.]

## Skill Version(s):

1.0.22 (source: ClawHub release; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
