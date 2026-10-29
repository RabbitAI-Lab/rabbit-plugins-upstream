## Description:

Analyzes a reference image’s composition, colors, lighting, and style, then generates a new image in a similar visual style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use this skill to turn a reference image into a new image with a similar visual style through dLazy’s hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to dLazy for cloud processing, and generation may consume account credits.

Mitigation: Submit only images and prompts you are comfortable sharing with dLazy, and use --dry-run to preview the estimated cost.

Risk: Login stores a reusable API key in the local CLI configuration.

Mitigation: Protect the local configuration file and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (not server-verified provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image asset and JSON result envelope with output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the image locally; asynchronous runs may return a task ID before the image is ready.]

## Skill Version(s):

1.3.36 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
