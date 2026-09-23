## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model. 使用 Grok 4.2 文本大模型，进行高效的文本生成、对话问答与逻辑推理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy Grok 4.2 hosted text model for text generation, dialogue question answering, and logical reasoning from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-supplied media paths may be sent to the third-party dLazy hosted service.

Mitigation: Install and use the skill only when third-party hosted inference is acceptable for the data being processed.

Risk: Authentication can persist a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when persistent CLI state is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on npm or npx and the pinned third-party dLazy CLI package.

Mitigation: Review the referenced package and source before installation, and prefer the pinned install or npx command listed in metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry-run and asynchronous task polling through the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
