## Description:

Generates speech from text with Qwen TTS using preset voices or a natural-language description of a custom voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users generate spoken audio from text, choosing a preset voice or describing a custom voice through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI requires a dLazy account and API key and may store credentials locally.

Mitigation: Review the CLI before installing it; protect stored credentials and rotate or revoke keys if needed.

Risk: Text prompts are sent to dLazy, and local media paths supplied by users may be uploaded.

Mitigation: Avoid sending sensitive text or media unless the service's data handling is acceptable.

Risk: The documented image-output example may misrepresent this text-to-speech skill's results.

Mitigation: Check actual responses for audio outputs rather than relying on the example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and generated audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated audio locally; the documented image-output example may be incorrect.]

## Skill Version(s):

1.3.22 (source: server release metadata; skill files list 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
