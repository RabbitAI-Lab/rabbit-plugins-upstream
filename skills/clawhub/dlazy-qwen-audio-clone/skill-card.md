## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to call dLazy's hosted Qwen audio clone workflow with an audio sample, name, and optional description, producing a cloned voice that can be reused in downstream text-to-speech calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends voice recordings and related request data to dLazy's hosted service, which can involve sensitive voice or biometric-like data.

Mitigation: Use only audio you own or have explicit permission to clone, confirm dLazy retention and usage terms, and avoid uploading sensitive recordings unless the service terms fit the use case.

Risk: Authentication can persist a dLazy API key in local CLI configuration.

Mitigation: Prefer npx or per-invocation DLAZY_API_KEY use when local persistence is undesirable, and rotate or revoke organization keys when access changes.

Risk: The current documentation contains confusing parameter and output examples for this audio-cloning workflow.

Mitigation: Check dlazy qwen-audio-clone -h and use dry-run or a low-risk sample before relying on generated commands in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI and hosted API; async runs may return a generateId for later polling.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
