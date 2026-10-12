## Description:

Transcribes video, translates speech into Chinese subtitles, burns them into an MP4, and optionally adds a time-aligned dub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to produce Chinese-subtitled video and, when requested, a dubbed version with speech fitted to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio are uploaded to dLazy services for processing.

Mitigation: Confirm that the selected media is appropriate to share with dLazy before running the workflow.

Risk: The recommended login flow stores a dLazy API key locally.

Mitigation: Use the documented DLAZY_API_KEY option if you prefer not to persist the key.

Risk: The documented translation workflow targets Simplified Chinese subtitles and dubbing.

Mitigation: Use it primarily for Chinese-language output and review the resulting subtitles and dub.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [MP4 video and SRT subtitle files, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitles are burned into the video; a time-aligned dub is produced only on request.]

## Skill Version(s):

1.0.20 (source: ClawHub release; skill frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
