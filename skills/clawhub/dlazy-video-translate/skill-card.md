## Description:

Transcribes video with word-level timings, translates subtitles, burns them into an MP4, and can optionally create a fitted dubbed audio track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn source videos into translated subtitle files and finished MP4 videos. When dubbing is requested, it also guides creation of timed speech segments and a replacement audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio content may be uploaded to dLazy hosted API and media services for processing.

Mitigation: Use this skill only for content appropriate for dLazy hosted processing and review applicable service terms before handling sensitive media.

Risk: The workflow requires a dLazy API key and may store credentials in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary credentials in shared environments and rotate or revoke keys when access should change.

Risk: The workflow can make billable API calls, especially when generating one text-to-speech segment per subtitle cue.

Mitigation: Use dry-run or credit estimates before long jobs and confirm available balance before requesting dubbing.

Risk: Global installation of the pinned CLI persists an executable on the system.

Mitigation: Prefer the pinned npx form or review the pinned CLI source before global installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and expected media and subtitle file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitles and MP4 video outputs; optional dubbing creates WAV segments and a dubbed MP4.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
