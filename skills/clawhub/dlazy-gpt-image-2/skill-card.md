## Description:

GPT Image 2 model for text-to-image and image editing, including generation from text and editing or synthesis with reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts and edit or synthesize images with reference inputs through the dLazy hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be sent to the dLazy hosted API and media storage.

Mitigation: Only pass prompts and files intended for upload to dLazy, and review service terms before use.

Risk: The skill depends on a third-party npm CLI and may store an API key in local user configuration.

Mitigation: Prefer npx for on-demand execution when possible, review the referenced CLI source and npm package, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns generated image metadata and hosted asset URLs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
