## Description:

Alibaba's flagship Qwen reasoning model is exposed through the dLazy CLI for text generation, complex reasoning, code engineering, long-context analysis, and prompts that include image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to call dLazy's hosted Qwen 3.8 Max model for generation, reasoning, code work, long-context analysis, and image-informed prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and optional uploaded files are sent to dLazy cloud services for inference.

Mitigation: Use only content approved for dLazy processing, and pass local files only when upload to dLazy media storage is intended.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, scope keys to the intended organization, and rotate or revoke keys when needed.

Risk: A global CLI install creates a persistent local dependency.

Mitigation: Review the dLazy CLI source before installing globally, or use the pinned npx form when a non-persistent invocation is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON result envelope from the dLazy CLI, with generated content in result.outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and optional upload of local image inputs to dLazy media storage.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
