## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can generate high-resolution images from text prompts or reference images for key visuals, posters, and print-ready work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and did not inspect the CLI package or confirm the documented image-generation behavior.

Mitigation: Review the CLI package and confirm its behavior before installing it or granting it credentials.

Risk: The documented login flow stores a dLazy API key locally, and prompts or local reference files are sent to the hosted service.

Mitigation: Use a revocable API key and submit only prompts and reference files appropriate for that service.

## Reference(s):

- [dLazy CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated image URLs in a JSON result, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolutions, several aspect ratios, up to 10 reference images, and asynchronous generation.]

## Skill Version(s):

1.2.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
