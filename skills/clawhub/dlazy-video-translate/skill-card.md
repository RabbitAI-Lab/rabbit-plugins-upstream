## Description:

Transcribes a video with word-level timings, translates the subtitles, burns them into the video, and optionally lays down a fitted dub track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate video speech into subtitles, burn those subtitles into an MP4, and optionally synthesize a timing-aligned dub track. It is intended for media localization workflows that can use dLazy cloud services, a dLazy API key, and local ffmpeg processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and local files supplied to the workflow are uploaded to dLazy services for processing.

Mitigation: Use only media that is appropriate for dLazy cloud processing and review service terms before handling sensitive content.

Risk: The workflow relies on a pinned external npm CLI and a dLazy API key stored or supplied by the user.

Mitigation: Review the pinned CLI package before installing, prefer device-code login over pasting keys into shell commands, and rotate or revoke keys when needed.

Risk: ffmpeg commands using -y can overwrite existing output files.

Mitigation: Review output filenames before execution and run commands from the intended working directory.

Risk: Some dLazy operations may consume paid credits.

Mitigation: Use dry-run or cost checks where available and confirm upload or paid-credit operations before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands and generated media/subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces SRT subtitle files and MP4 outputs; dubbing is optional and only used when requested.]

## Skill Version(s):

1.0.6 (source: server release metadata, released 2026-09-07; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
