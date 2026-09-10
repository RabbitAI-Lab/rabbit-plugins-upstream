## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the dLazy image-replicate CLI, analyze a reference image, and generate a new image with similar visual style through the hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and image inputs to dLazy-hosted API and media storage endpoints.

Mitigation: Only use image files intended for upload to dLazy and confirm the service is appropriate for the data before invocation.

Risk: Authentication uses a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config and environment, and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

Risk: Global installation of the CLI persists a binary on the host.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 invocation path when a persistent global binary is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown command guidance with JSON CLI responses and optional generated image files or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; image inputs may be uploaded to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
