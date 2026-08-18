## Description:

Generates ecommerce model-look images by combining up to eight apparel and accessory product images into one styled outfit, with optional pose, scene, lighting, and model references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, merchandisers, and marketing creators use this skill to turn multiple product images into a complete model-worn look for shop listings, look books, bundle images, and cross-category campaign assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image files passed to the workflow are uploaded to dLazy's hosted service for inference.

Mitigation: Use only product, reference, and model images the user is authorized to upload, and review dLazy service terms before operational use.

Risk: The dLazy CLI may store an API key in local user configuration.

Mitigation: Use organization-scoped keys, restrict local account access, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: A fixed default model description can override user intent for demographics or appearance.

Mitigation: Replace sample demographics and appearance text with user-provided requirements when those attributes matter.

Risk: Generated model imagery could be misused to imply a real person's endorsement.

Mitigation: Do not use the workflow to fabricate another person's portrait endorsement, and review outputs before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/image-fusion)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated-image URLs and optionally save generated image files through the dLazy CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
