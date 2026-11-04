## Description:

Generates Midjourney-style images with configurable aspect ratios, bot types, and grid or upscaled outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request stylized image generation through dLazy's hosted service, choosing an aspect ratio, Midjourney or Niji Journey bot, and grid or upscaled result. They need a dLazy API key, and generation may incur service charges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media are sent to dLazy services; local media may be uploaded for processing.

Mitigation: Use device-code login and submit only prompts and media you intend to share with dLazy.

Risk: The CLI stores an API key in the local user configuration, and image generation may incur service charges.

Mitigation: Protect the local configuration, rotate or revoke an exposed key, and review service charges before generating.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image assets with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratio and grid or U1-U4 output selection.]

## Skill Version(s):

1.3.36 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
