## Description:

Transcribes a video with word-level timings, translates the subtitles, burns them into the video, and optionally adds a fitted dub track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate local video files into subtitle-burned MP4 outputs and, when requested, generate an aligned dubbed audio track. It is intended for workflows that can use dLazy API-backed speech, translation, and TTS services alongside local ffmpeg processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and local files passed to the workflow are uploaded to dLazy services for processing.

Mitigation: Use the skill only for media that may be sent to dLazy, and confirm before running broad video translation requests.

Risk: The workflow uses paid API-backed tools and can spend credits, especially when dubbing calls TTS once per subtitle cue.

Mitigation: Use dry-run or cost checks where available and confirm credit impact before long videos or dubbing runs.

Risk: Persistent CLI authentication stores an API key in the user's local dLazy configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, or review the CLI before storing credentials.

Risk: Global npm installation persists an external CLI on the user's machine.

Mitigation: Prefer the pinned npx invocation or review the dLazy CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, SRT subtitle files, and MP4 media outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, ffmpeg, ffprobe, a dLazy API key, and access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
