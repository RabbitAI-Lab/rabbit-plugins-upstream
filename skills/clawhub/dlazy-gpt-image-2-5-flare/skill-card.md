## Description:

GPT Image 2.5 Flare is a fast, cost-effective image generation and editing option that supports reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate or edit images from text prompts and optional reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's hosted service; its retention practices were not verified.

Mitigation: Avoid sending sensitive or private material unless you are comfortable sharing it with dLazy.

Risk: The CLI saves an API key locally, and its credential-file protections were not verified.

Mitigation: Use a dedicated key, protect access to the local account, and rotate or revoke the key if it may have been exposed.

Risk: Image generation may incur usage charges.

Mitigation: Review the service's current pricing and your expected usage before generating images.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Generated image assets returned through hosted URLs, with JSON task metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and up to five reference images; supports automatic or preset aspect ratios through 21:9 and quality settings from low to max.]

## Skill Version(s):

1.2.26 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
