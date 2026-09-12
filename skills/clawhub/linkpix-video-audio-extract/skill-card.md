## Description:

Extracts audio from local video files or supported shared video links into MP3 or WAV files using ffmpeg, with optional qhkit link resolution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to convert video files or supported shared video links into reusable MP3 or WAV audio outputs for editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install and execute a global third-party CLI.

Mitigation: Review the qhkit tool before use, prefer a sandboxed or local install, and pin the package version when possible.

Risk: The workflow may require an API token for link resolution.

Mitigation: Do not paste production tokens into chat; configure a least-privilege, revocable token locally and rotate it after use.

Risk: The workflow mentions an alternate npm registry for slow or timed-out installs.

Mitigation: Use the default registry when possible and use alternate registries only after confirming they are trusted.

Risk: Extracted music or background audio may have copyright restrictions, especially for commercial reuse.

Mitigation: Confirm rights and licensing before using extracted audio in commercial work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-audio-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu website](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples and local audio file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MP3 or WAV audio files when commands are executed in an environment with ffmpeg and any required link-resolution tooling.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
