## Description:

Generate and edit high-quality images with Nano Banana 2.0 for text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Nano Banana 2 image-generation CLI for prompt-based image creation and editing, including optional local or URL image inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a global npm CLI adds persistent third-party code to the local environment.

Mitigation: Use the pinned npx invocation or a sandboxed environment when a persistent global install is not required.

Risk: API keys may be stored in the dLazy CLI user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY in sensitive environments and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Prompts, parameters, and selected local media are sent to dLazy-hosted services for generation.

Mitigation: Confirm that selected files are appropriate to upload before invoking image-to-image workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated image URLs or asynchronous task identifiers through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
