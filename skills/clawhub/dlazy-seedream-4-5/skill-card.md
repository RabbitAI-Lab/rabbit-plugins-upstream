## Description:

Generates high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users creating visual assets can generate images from text prompts or supplied reference images with Doubao Seedream 4.5 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to dLazy's hosted service, and generation uses credits.

Mitigation: Send only prompts and images you are comfortable sharing with the service, and review the cost estimate or your available credits before generating.

Risk: Logging in saves the API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment variable for per-invocation authentication if you prefer not to save the key locally; rotate or revoke the key when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy API endpoint](https://api.dlazy.com)
- [dLazy media storage](https://files.dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-to-image and image-to-image; 2K or 4K resolution, selectable aspect ratios, up to 10 reference images, and optional asynchronous status output.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
