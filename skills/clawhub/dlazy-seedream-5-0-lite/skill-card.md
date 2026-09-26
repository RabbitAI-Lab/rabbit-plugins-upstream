## Description:

Provides fast image generation with Doubao Seedream 5.0 Lite for text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images through dLazy's hosted Seedream 5.0 Lite API from prompts and optional input images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy's hosted service for generation.

Mitigation: Use the skill only with content approved for dLazy cloud processing, and avoid passing sensitive local files.

Risk: Login can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY credentials or npx for less persistent use, and rotate or revoke keys when needed.

Risk: The skill depends on the third-party dLazy CLI and cloud endpoints.

Mitigation: Install the pinned CLI version from the declared package source and review the service terms and source links before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [JSON with generated image URLs; optional downloaded image files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs when --no-wait is used.]

## Skill Version(s):

1.3.19 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
