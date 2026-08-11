## Description:

Alibaba Bailian qwen3-tts text-to-speech that can use curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's Qwen TTS CLI, generate speech from text, select system voices or design a voice from a natural-language description, and receive the resulting hosted output or async task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to dLazy's hosted API for inference.

Mitigation: Avoid submitting private or regulated text unless the user intends to send it to dLazy's service.

Risk: API use may consume dLazy account credits.

Mitigation: Use dry-run or review cost information when available, and tell the user to recharge only when the service reports insufficient balance.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard if needed.

Risk: A global CLI install leaves a persistent binary on the system.

Mitigation: Use the pinned npx invocation when the user does not want a persistent global CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an async generateId for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
