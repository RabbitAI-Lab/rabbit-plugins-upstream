## Description:

Guides agents in creating realistic on-model accessory product photos from product and model reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to guide image generation that places shoes, bags, jewelry, eyewear, and other accessories on a model while preserving product details and the reference scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model images and prompts are sent to the selected cloud provider.

Mitigation: Use only images and prompts approved for that provider; review configured provider credentials before generation.

Risk: Untrusted image URLs or unintended output paths may expose data or write files locally.

Mitigation: Use trusted local images or public URLs and review the output destination before saving.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be saved to a user-selected local path.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
