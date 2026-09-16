## Description:

This skill analyzes an input image's visuals, composition, colors, lighting, and style, builds a replication prompt, and invokes Seedream 4.5 through the dLazy CLI to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to replicate the visual style of source images through dLazy's hosted image generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on external dLazy CLI code that is not included in the skill package.

Mitigation: Install only if dLazy and the pinned @dlazy/cli package are trusted; prefer npx @dlazy/cli@1.2.3 over a persistent global install.

Risk: Prompts and local image files passed to the command are sent to dLazy hosted services.

Mitigation: Pass only files intended for upload and use a dLazy API key that can be rotated or revoked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI repository declared in metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [JSON response with generated image URLs; optional saved image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local image inputs are uploaded to dLazy media storage; async mode can return a generateId for polling.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
