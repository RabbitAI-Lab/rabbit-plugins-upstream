## Description:

Transcribes video, translates timed subtitles, burns them into an MP4, and optionally adds a synchronized dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and localization teams use this skill to produce translated SRT subtitles and subtitled videos, with optional dubbed video when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video or audio content is uploaded to dLazy cloud services for processing.

Mitigation: Obtain permission to process the content and review dLazy's handling of uploaded media before using sensitive footage.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the local key, or supply DLAZY_API_KEY per run instead of storing it.

Risk: Transcription, translation, and optional per-cue dubbing consume paid API credits.

Mitigation: Review credit estimates with the documented dry-run option before processing a video.

Risk: The workflow depends on the third-party @dlazy/cli package.

Mitigation: Review the pinned package source before installation if stronger assurance is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source code (tool dependency, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Files]

**Output Format:** [SRT subtitles and subtitled MP4; optional dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dubbing runs only when requested.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
