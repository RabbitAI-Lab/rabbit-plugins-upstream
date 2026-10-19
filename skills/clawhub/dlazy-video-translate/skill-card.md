## Description:

Transcribes and translates video speech into timed subtitles, burns them into an MP4, and optionally adds a timing-matched dubbed audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and localization teams use this skill to translate video speech, generate timed subtitle files and a subtitled MP4, and optionally dub the video into another language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video or audio is uploaded to dLazy for processing, which may expose sensitive media to a third-party service.

Mitigation: Confirm approval to share the media and review its sensitivity before processing.

Risk: Logging in stores an API key locally for later use.

Mitigation: Prefer a per-invocation DLAZY_API_KEY when persistent credentials are undesirable; rotate or revoke saved keys as needed.

Risk: Transcription, translation, and optional per-segment dubbing can consume paid credits.

Mitigation: Confirm the requested workflow and expected costs before processing, especially before optional dubbing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI repository (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Burned-in translated subtitles; a fitted dubbed audio track is optional.]

## Skill Version(s):

1.0.23 (source: server-resolved ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
