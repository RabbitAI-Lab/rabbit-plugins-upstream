## Description:

Extracts MP3 or WAV audio from local videos or direct video URLs, and can use qhkit to resolve supported platform share links before extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, and agents use this skill to extract background music, speech tracks, or other audio from video for editing workflows. For platform share links, it resolves a playable video URL with qhkit before running ffmpeg.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit link parser can create paid or credit-consuming tasks.

Mitigation: Require explicit user confirmation before running qhkit commands that submit parsing jobs, including the target link and that actual credit usage may apply.

Risk: Global ffmpeg or qhkit installation and qhkit API tokens can affect the host environment or expose credentials if used in an untrusted environment.

Mitigation: Confirm the environment is trusted before installing tools or configuring qhkit tokens, and avoid sharing tokens outside the active setup flow.

Risk: Extracted music or audio may be subject to copyright restrictions, especially for commercial reuse.

Mitigation: Warn users to confirm rights before commercial use of extracted BGM or other protected audio.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / Qinghu workspace](https://www.iqinghu.com)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [qhkit setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with bash command examples and local audio file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MP3 or WAV audio files; may also surface a parsed videoScript when useful.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
