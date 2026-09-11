## Description:

Extracts audio, background music, or spoken audio from local video files or supported platform share links into MP3 or WAV, using ffmpeg and qhkit when link resolution is needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to convert local videos or supported platform share links into MP3 or WAV audio files for editing and content workflows. It can also return the local file path and optional extracted video script when useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may ask users to provide a production qhkit API token through chat or logs.

Mitigation: Configure the token locally instead of pasting it into conversation, and revoke or rotate any token that was exposed.

Risk: The setup flow installs an unpinned global npm CLI.

Mitigation: Install a reviewed, pinned qhkit version from the official registry before using the skill.

Risk: Extracted background music or audio may be subject to copyright restrictions, especially for commercial reuse.

Mitigation: Confirm usage rights before distributing or commercializing extracted audio.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-audio-extract)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown with inline bash commands and local audio file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MP3 or WAV audio files and may include extracted videoScript text when available.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
