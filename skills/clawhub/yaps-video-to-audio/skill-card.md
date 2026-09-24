## Description:

Save the sound from a video as MP3, WAV, or M4A with Yaps. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

Developers and users use this skill to extract a requested audio track from a local video file through the Yaps desktop engine while preserving the source video and existing exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that the bundled runner exposes broader Yaps commands, transcription, subtitles, and meeting processing beyond the advertised video-to-audio purpose.

Mitigation: Use it only for explicit video-to-audio extraction requests, inspect generated Yaps commands, and avoid unrelated Yaps workflows.

Risk: Unexpected account, Keychain, download, or broader Yaps workflow prompts could expand the operation beyond simple audio extraction.

Mitigation: Do not approve unexpected prompts; authorize installs or downloads only after the agent explains why they are needed for the requested extraction.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with inline shell commands; successful runs produce local MP3, WAV, or M4A audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Yaps 2.3.124 or newer, Node.js 22 or newer, account readiness for gated tasks, and user authorization for any dependency download.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
