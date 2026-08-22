## Description:

Extracts BGM, speech, and other audio from local videos or supported platform share links into MP3/WAV, using ffmpeg locally and qhkit link resolution when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and agent users use this skill to extract reusable audio tracks from local videos or from share links after resolving them to direct media URLs. It is suited for content editing workflows where the agent should produce an audio file path and, when available, related video script text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit video-inspire generate path can consume credits when resolving a platform share link.

Mitigation: Require explicit user confirmation before submitting the qhkit task, including the target link and that actual credit use may vary.

Risk: qhkit configuration may require an API token outside the OpenClaw environment.

Mitigation: Review token setup before use and avoid exposing API keys in prompts, logs, or generated output.

Risk: Extracted music or speech may be subject to copyright, privacy, or platform terms.

Mitigation: Remind users to confirm they have rights to reuse extracted audio, especially for commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-audio-extract)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / Qinghu workspace](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and generated audio file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MP3 or WAV audio files; may also return videoScript text when qhkit provides it.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
