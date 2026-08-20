## Description:

Retouches ecommerce product photos by reducing random wrinkles, improving flat-lay symmetry, evening lighting, cleaning backgrounds, improving clarity, and preserving the item's style, color, pattern, hardware, and structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, content teams, and agents use this skill to turn casual or warehouse product photos into catalog-ready retouched images while preserving the represented product. It is most useful for flat-lay garments, wrinkle cleanup, general product-photo cleanup, background purification, and multi-angle product retouching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are uploaded to dLazy cloud services for inference.

Mitigation: Use the skill only with images approved by the user's data policy, especially for confidential or unreleased products.

Risk: The dLazy CLI may store an API key locally when configured with persistent login.

Mitigation: Use per-invocation credentials when persistent local storage is not acceptable, and rotate or revoke keys when needed.

Risk: Retouching can unintentionally hide defects or alter product representation.

Mitigation: Review outputs before publication and use prompts that preserve holes, stains, damage, structure, color, pattern, and hardware.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [dLazy](https://dlazy.com)
- [dLazy CLI source code](https://github.com/dlazyai/cli)
- [Related material enhancement workflow](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted dLazy output URLs and save retouched product image files through the dLazy CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
