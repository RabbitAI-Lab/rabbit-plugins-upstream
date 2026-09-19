## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate high-resolution raster images through the dLazy Recraft V4 Pro service. It supports prompt-driven image generation, optional aspect-ratio control, asynchronous generation, and saving generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media are sent to dLazy services for inference, and generated assets are hosted by dLazy.

Mitigation: Use only prompts and media approved for a third-party cloud image-generation service, and review dLazy data handling before use.

Risk: The dLazy CLI requires an API key that can be stored in a local CLI configuration file.

Mitigation: Prefer environment-scoped credentials where appropriate, protect the local config file, and rotate or revoke keys if exposure is suspected.

Risk: Using this skill requires trust in the dLazy npm CLI and hosted service.

Mitigation: Confirm the CLI package and publisher before installing or running it, and use the pinned package version declared by the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, API Calls, Shell commands, Configuration instructions]

**Output Format:** [JSON response with generated image URLs, or downloaded PNG files when a save path is provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; asynchronous requests can return a generation ID for later polling.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
