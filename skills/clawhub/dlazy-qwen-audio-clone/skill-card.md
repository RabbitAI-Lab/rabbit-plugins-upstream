## Description:

Alibaba Bailian qwen3-tts voice cloning that uploads a clean voice sample to create a custom voice usable in later text-to-speech calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Qwen audio cloning workflow, supplying a clean voice sample and metadata to create a reusable custom voice for later text-to-speech calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may control paid credits or sensitive organization access and can be stored in a local CLI configuration file.

Mitigation: Prefer per-command DLAZY_API_KEY for sensitive use, or verify that ~/.dlazy/config.json is readable only by the current OS user; rotate or revoke keys from the dLazy dashboard when needed.

Risk: The inspected CLI did not fully support the artifact's file-permission claim for stored credentials.

Mitigation: Review local permissions after authentication before using organization-scoped API keys on shared systems.

Risk: The artifact examples do not match the qwen-audio-clone help text, which can lead to failed or unintended invocations.

Mitigation: Run dlazy qwen-audio-clone -h and use dry-run behavior where available before submitting paid or sensitive jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
