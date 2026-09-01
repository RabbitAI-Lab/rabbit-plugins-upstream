## Description:

Transcribes videos with word-level timing, translates subtitle cues, burns translated subtitles into an MP4, and optionally creates a fitted dub track using dLazy cloud tools with local ffmpeg processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to translate video speech into subtitle files and finished MP4 outputs, with optional dubbing when the user asks for a replacement audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, and generated text are sent to dLazy cloud services for processing.

Mitigation: Use this skill only when that transfer is acceptable for the content being processed.

Risk: The workflow writes common output filenames such as track.wav, trans.srt, output_sub.mp4, and dubtrack.wav in the working directory.

Mitigation: Run the workflow in a dedicated project directory to avoid overwriting unrelated files.

Risk: Long-lived API keys may be saved in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when reduced local persistence is preferred, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON/SRT file handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for creating SRT subtitles, MP4 files with burned subtitles, and optional dubbed audio/video outputs.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
