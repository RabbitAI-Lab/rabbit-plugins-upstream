## Description:

Extracts audio from local video files or direct video URLs with ffmpeg, and can use qhkit to resolve supported platform share links before extracting MP3 or WAV audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, editors, and agents use this skill to extract background music, speech, or other audio tracks from video assets for editing and content production. It is suited to local video files, direct video URLs, and supported share links that can be resolved through qhkit after user confirmation for credit-consuming tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: qhkit setup may store an API token locally.

Mitigation: Use qhkit only in trusted environments and avoid sharing local configuration or tokens.

Risk: Submitting a qhkit video-inspire task can consume credits.

Mitigation: Tell the user which link will be parsed, explain that actual charges apply, and wait for explicit consent before running the generate command.

Risk: Extracted music or speech may be subject to copyright or platform reuse restrictions.

Mitigation: Remind users to confirm rights before commercial reuse of extracted audio.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-audio-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu workspace](https://www.iqinghu.com)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [qhkit setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local MP3 or WAV audio files when executed in an environment with ffmpeg and any required qhkit setup.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
