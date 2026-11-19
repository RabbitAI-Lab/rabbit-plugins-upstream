## Description:

Alibaba Bailian Qwen3-TTS text-to-speech using curated system voices or custom voice descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate speech from text with a selected system voice or a voice described in natural language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the CLI login and authentication step as unexplained relative to the advertised speech-generation behavior; the scan did not inspect the CLI.

Mitigation: Review and trust the CLI and its login/API-key flow before use; use an organization key you trust and rotate or revoke it if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON results with generated audio URLs or asynchronous task status, plus Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier before generated outputs are available.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
