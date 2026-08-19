## Description:

Generates on-model commercial accessory photos by placing shoes, bags, watches, glasses, hats, scarves, jewelry, and similar products onto a human reference image while preserving the product appearance and the rest of the scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agent users use this skill to prepare product-on-model accessory imagery from a product photo and a human reference photo. It is suited for replacing or supplementing live accessory photography for catalog images, social commerce, and product marketing review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided product and model photos are uploaded to the dLazy service for hosted image generation.

Mitigation: Use only images the user has rights and consent to process, and avoid uploading sensitive or restricted photos.

Risk: The dLazy CLI can store an API key in local user configuration.

Mitigation: Use revocable API keys, rotate keys when needed, or provide credentials per invocation through DLAZY_API_KEY when persistent local storage is not desired.

Risk: Generated images may alter likeness, placement, scale, reflections, or surrounding scene details in ways that affect commercial accuracy.

Mitigation: Review outputs before publication, use the skill's placement and preservation prompt constraints, and do not use outputs to imply a person's endorsement or identity without authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Related flat-lay skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Wear Everything example output](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/wear-everything/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, JSON examples, and generated image file or URL outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product and model reference images, dLazy API authentication, size and quality options, optional batch generation, and optional local save paths.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
