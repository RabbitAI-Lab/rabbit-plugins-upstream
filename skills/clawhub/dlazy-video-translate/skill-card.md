## Description:

Transcribes videos with word-level timings, translates subtitle cues, burns translated subtitles into the video, and optionally creates a fitted dubbed audio track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and localization teams use this skill to turn source videos into translated, subtitled MP4 outputs and, when requested, dubbed videos aligned to the original timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy media storage and processed through dLazy API endpoints.

Mitigation: Use the skill only for media that may be sent to dLazy, and review the service terms before processing sensitive content.

Risk: The workflow can consume paid dLazy credits for transcription, translation, and per-cue TTS calls.

Mitigation: Use dry-run when possible and confirm available credits before running long videos or dubbing jobs.

Risk: A dLazy API key may be stored locally or passed through the DLAZY_API_KEY environment variable.

Mitigation: Use the CLI authentication flow or a local secret store, avoid pasting keys into chat or logs, and rotate or revoke keys when needed.

Risk: Global npm installation adds a third-party CLI to the user's environment.

Mitigation: Prefer npx or a non-privileged environment when evaluating the skill, and review the @dlazy/cli package and source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON response paths, and expected SRT and MP4 file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Composes local ffmpeg/ffprobe commands with dLazy API-backed transcription, translation, and optional TTS calls.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
