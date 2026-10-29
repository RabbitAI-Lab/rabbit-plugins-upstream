## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative professionals use the skill to generate high-resolution raster images from text prompts for print-ready assets and large-format use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation can spend dLazy credits.

Mitigation: Review the prompt and cost estimate before submitting a generation request.

Risk: Prompts and supplied media are sent to dLazy, and local media may be uploaded for processing.

Mitigation: Submit only prompts and media that are appropriate to share with the service.

Risk: The organization API key is stored in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key from the organization dashboard if needed.

Risk: The skill relies on an installed CLI package.

Mitigation: Review the pinned CLI package before installation; use the documented on-demand npx option to avoid a persistent global install.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Raster image files (PNG) with a hosted result URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 4MP; supports asynchronous generation and local saving]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
