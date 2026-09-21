## Description:

Transcribes video into word-timed captions, translates subtitles, burns them into an MP4, and optionally creates a timing-fitted dubbed audio track using dLazy tools and local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media operators use this skill to produce translated subtitle files and finished MP4 videos from source videos. It can also generate a fitted dub track when dubbing is explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio files are uploaded to dLazy services for processing.

Mitigation: Confirm the user is comfortable sending the media to dLazy before running the workflow, especially for sensitive or restricted content.

Risk: The workflow can spend dLazy credits for transcription, translation, and text-to-speech calls.

Mitigation: Use dry-run or explicit confirmation before billed steps, and batch subtitle translation into one call as the skill describes.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY or pinned npx invocation when a saved credential or global install is not desired; rotate or revoke saved keys when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and file-output instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of SRT subtitle files, subtitle-burned MP4 files, and optional dubbed MP4 files.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
