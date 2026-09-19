## Description:

GPT Image 2.5 Flare is the speed tier of OpenAI's GPT Image 2.5 series for text-to-image generation and image editing, supporting reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy CLI using GPT Image 2.5 Flare, with prompts, optional reference images, aspect ratio controls, quality settings, and local save support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media files are sent to dLazy's hosted service for generation.

Mitigation: Review prompts and media before use, and avoid sending sensitive or restricted content unless that use is approved for the environment.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the documented login or auth setup intentionally, protect the local configuration file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the third-party dLazy npm package and hosted endpoints.

Mitigation: Review the pinned package/source and endpoint use before installing in environments with supply-chain or data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [JSON responses with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generateId when no-wait mode is used.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
