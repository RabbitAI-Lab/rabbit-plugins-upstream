## Description:

Transcribes video speech, translates timed subtitles, burns them into the video, and can add a timing-fitted dubbed track when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and localization teams use this skill to translate video speech into target-language subtitles and optionally produce a dubbed version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default media commands can replace existing files without asking.

Mitigation: Work in a fresh output folder and check that target filenames do not already exist before running the commands.

Risk: Video audio and subtitle text are uploaded to dLazy for processing.

Mitigation: Use only media approved for upload and tell users where their content will be processed.

Risk: Processing consumes account credits, and the API key is normally saved in the user's dLazy configuration.

Mitigation: Use the documented dry-run option to review requests and estimated credits; keep the configuration file private and rotate the key if exposed.

Risk: The documented translation prompt specifies Simplified Chinese, which may not match the user's intended target language.

Mitigation: Confirm the target language before processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, SRT subtitle files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include a dubbed audio track when requested.]

## Skill Version(s):

1.0.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
