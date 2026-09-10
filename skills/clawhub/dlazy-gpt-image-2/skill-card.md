## Description:

GPT Image 2 generates images from text and edits or synthesizes images using reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the dLazy GPT Image 2 CLI for text-to-image generation, image editing, and image synthesis with reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media to dLazy hosted API services.

Mitigation: Only provide prompts and media files that are appropriate to send to dLazy's hosted service.

Risk: The dLazy CLI stores an API key in the user's local configuration or accepts it through an environment variable.

Mitigation: Protect the API key, scope access to the intended organization, and rotate or revoke the key when needed.

Risk: The skill depends on executing the pinned @dlazy/cli package.

Mitigation: Review the linked source or npm package before use in sensitive environments and prefer npx or an isolated install over a privileged global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce hosted image result URLs, asynchronous task IDs, or downloaded image assets when a save path is provided.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
