## Description:

Generate and edit high-quality images with Nano Banana 2.0 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or edit images from text prompts and reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service, and local reference files are uploaded for processing.

Mitigation: Upload only prompts and images you are comfortable sharing with dLazy.

Risk: Image generation may incur service charges, and API credentials are stored in a local CLI configuration when using device login.

Mitigation: Review the CLI cost estimate before submitting requests, and keep API keys out of chat; use device login or the documented environment-variable option.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Image URLs, JSON response]

**Output Format:** [Generated PNG images returned as hosted URLs, with an option to save files locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image generation or editing.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
