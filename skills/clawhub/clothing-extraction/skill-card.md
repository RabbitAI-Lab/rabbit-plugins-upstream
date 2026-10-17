## Description:

Guides the extraction of a single garment from a photo into a clean, white-background product flat-lay image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to prepare flat-lay product imagery from model photos, street photos, or customer images. Each run isolates one item and proposes prompts and commands for image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, prompts, and generated outputs are sent to the selected cloud image provider.

Mitigation: Use private or sensitive photos only after checking the provider's privacy and retention terms.

Risk: Occluded garment features may be inferred inaccurately in generated product images.

Mitigation: Manually compare inferred areas and key product details against the source before publishing.

## Reference(s):

- [Clothing Extraction on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands generates product flat-lay image files; concealed garment details are inferred and require review.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
