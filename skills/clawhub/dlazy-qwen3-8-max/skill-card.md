## Description:

Alibaba's flagship Qwen reasoning model (2.4T-parameter MoE), strong at complex reasoning, code engineering and long-context analysis. Accepts text and image input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can invoke the dLazy CLI to send text prompts and optional image inputs to the hosted Qwen 3.8 Max model for reasoning, code engineering, and long-context analysis tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a dLazy API key locally and security evidence says the file-permission protection is overstated.

Mitigation: Prefer per-invocation DLAZY_API_KEY or manually restrict permissions on ~/.dlazy/config.json, and rotate the key if it may have been exposed.

Risk: Prompts and any local media files explicitly passed to the command are sent to dLazy endpoints for hosted inference and storage.

Mitigation: Install and use the skill only when sharing those prompts and files with dLazy is acceptable for the user and organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON response from the dLazy CLI, with generated text or task status returned in the result envelope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous calls can return a generateId for later polling.]

## Skill Version(s):

1.2.9 (source: server-resolved release metadata; artifact frontmatter and install spec pin dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
