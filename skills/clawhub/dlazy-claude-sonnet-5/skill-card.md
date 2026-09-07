## Description:

This skill routes text, image, and video prompts through the dLazy CLI to Anthropic's Claude Sonnet 5 model for reasoning, code generation, and tool-oriented tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Claude Sonnet 5 generation workflow from an agent. It supports text prompts plus optional image and video inputs for reasoning, code generation, and complex tool orchestration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI and hosted service receive prompts, selected media files, and a dLazy API key.

Mitigation: Use the documented authentication flow, pass only files intended for upload, and rotate or revoke the API key when access is no longer needed.

Risk: Global installation persists a third-party npm CLI on the user's system.

Mitigation: Use the documented npx invocation for on-demand use, or review the linked source and package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI homepage metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses from the dLazy CLI, with agent-facing text or code content in returned outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when invoked with no-wait mode.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
