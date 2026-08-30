## Description:

Provides agent access to dLazy's hosted Qwen 3.8 Max model for reasoning, code engineering, long-context analysis, and text or image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to call dLazy's hosted Qwen 3.8 Max model for prompt-based text generation, reasoning, code work, and multimodal analysis with optional image inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy's hosted service.

Mitigation: Only pass prompts and files that are approved for processing by dLazy's hosted API.

Risk: The dLazy CLI may save an API key in the local user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local credential storage is not desired, and rotate or revoke keys through the dLazy dashboard when needed.

Risk: The skill relies on an npm-distributed CLI package.

Mitigation: Review the dLazy CLI source or package before installation when strict supply-chain controls apply.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI package repository](https://github.com/dlazyai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON envelope containing model outputs; content may be text, markdown, code, shell commands, configuration, or guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The command accepts a prompt and up to 10 image inputs; asynchronous invocations may return a task identifier for later polling.]

## Skill Version(s):

1.2.6 (source: server release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
