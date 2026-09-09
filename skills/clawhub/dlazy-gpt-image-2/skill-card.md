## Description:

Generates images from text and edits or synthesizes images with GPT Image 2 using optional reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to call the dLazy CLI for text-to-image generation and reference-image editing workflows. It is useful when an agent needs generated image URLs or saved image assets as part of a broader task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key that may be stored locally or supplied through the environment.

Mitigation: Use a revocable organization-scoped key, restrict local access to the config file, and rotate or revoke the key if exposure is suspected.

Risk: Reference image files passed to the CLI can be uploaded to dLazy's hosted media service.

Mitigation: Only provide files that are appropriate to upload to the service and review applicable service terms before using sensitive content.

Risk: A global CLI installation creates a persistent local binary.

Mitigation: Use the pinned on-demand npx command when a persistent global install is not needed, and review the linked source or npm package before installation.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)

## Skill Output:

**Output Type(s):** [JSON, Image files, Shell commands, Configuration guidance]

**Output Format:** [JSON response with generated image URLs; optional downloaded image file when a save path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload reference image files to dLazy's hosted service.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
