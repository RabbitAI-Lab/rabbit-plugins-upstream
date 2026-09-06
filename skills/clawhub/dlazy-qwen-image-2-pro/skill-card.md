## Description:

Alibaba Bailian qwen-image-2.0-pro image generation through the dLazy CLI, supporting prompts, optional reference images, multiple output sizes, and generated image URLs or saved files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images with Alibaba Bailian qwen-image-2.0-pro from an agent workflow through the dLazy hosted API. It is suited for prompt-based image generation, mixed text/image designs, and optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any reference files passed to the skill are sent to dLazy's hosted API and optional media storage.

Mitigation: Avoid submitting private or sensitive prompts and media unless the user accepts upload to the provider service.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Protect the local config file, prefer per-invocation environment variables where appropriate, and rotate or revoke keys from the provider dashboard when needed.

Risk: The skill installs or invokes a third-party npm CLI package.

Mitigation: Use the pinned npx invocation for less persistent execution or review the referenced CLI source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with generated image asset URLs, with optional local file output when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; async mode can return a generation task ID for later polling.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
