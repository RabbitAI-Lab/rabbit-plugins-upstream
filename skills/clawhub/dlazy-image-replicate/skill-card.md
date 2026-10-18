## Description:

Analyzes a reference image's composition, colors, lighting, and style, then uses Seedream 4.5 to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to create new images based on a reference image's visual style through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media and prompts may be uploaded to dLazy, and generated images are hosted by dLazy.

Mitigation: Use only media and prompts you are comfortable sharing with the hosted service.

Risk: Login or manual authentication can save a dLazy API key on the local device.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication when local persistence is undesirable; rotate or revoke keys in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image URLs]

**Output Format:** [CLI commands and JSON response with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a generated image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
