## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who create images use this skill to turn text prompts into Jimeng images, with optional reference images and size settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy hosted services for generation.

Mitigation: Send only prompts and images you are comfortable processing through dLazy.

Risk: Logging in stores an API key in the local CLI configuration, and generation uses service credits.

Mitigation: Use the documented DLAZY_API_KEY environment variable if you prefer not to save a key locally, and monitor or rotate credentials through the dLazy dashboard.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files or JSON results containing image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images (up to 10), image dimensions, asynchronous task status, and saving results to a local path.]

## Skill Version(s):

1.3.35 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
