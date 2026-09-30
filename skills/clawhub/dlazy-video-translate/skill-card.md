## Description:

Transcribes and translates video subtitles, burns them into an MP4, and optionally adds a timing-matched dub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and localization teams use this skill to produce translated subtitle files and subtitled videos, with a dubbed video when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video audio or other submitted media is sent to dLazy's cloud service.

Mitigation: Obtain permission to upload the media and check the service terms before processing sensitive content.

Risk: Signing in may save a dLazy API key locally.

Mitigation: Use DLAZY_API_KEY for per-run credentials if persistent storage is unwanted, and protect the key.

Risk: Translation and dubbing quality may vary, particularly outside Chinese subtitle workflows.

Mitigation: Review the translated subtitles and listen to the dub before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Workflow guidance, Shell commands, Video files, Subtitle files]

**Output Format:** [Instructions and commands yielding MP4 video and SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dubbing is optional and only performed when requested.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
