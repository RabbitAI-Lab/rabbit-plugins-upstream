## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis, with text and image input support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users invoke this skill to send prompts, optional image inputs, and generation settings to the dLazy-hosted Qwen 3.8 Max model for reasoning, code engineering, and long-context analysis tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media may be sent to dLazy cloud services for inference.

Mitigation: Avoid sending sensitive content unless the user has approved dLazy processing for that data.

Risk: Authentication stores a dLazy API key in local CLI configuration or reads it from DLAZY_API_KEY.

Mitigation: Use OS-level file permissions, avoid exposing the key in logs, and rotate or revoke the key from dLazy if it may be compromised.

Risk: The skill depends on a third-party npm CLI and hosted service.

Mitigation: Confirm trust in the @dlazy/cli package and dLazy service before installation or execution.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON result envelope from the dLazy CLI, often containing generated text or structured model output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation IDs, optional result download via --save, and dry-run cost estimation.]

## Skill Version(s):

1.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
