## Description:

Helps create on-model ecommerce images of shoes, bags, and accessories from product photos and model reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use this skill to place product accessories onto a model reference image while checking fit, product details, lighting, and preservation of the original scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model photos, prompts, and brand constraints may be sent to the selected cloud provider.

Mitigation: Use dry-run first and select an approved provider before sharing sensitive assets.

Risk: Provider credentials and installed CLI packages can expose access or incur charges if not managed carefully.

Mitigation: Keep API keys scoped and revocable, and prefer pinned trusted CLI packages.

Risk: Generated images may misrepresent product details or imply an unauthorized endorsement.

Mitigation: Review product fidelity and model likeness before publication; do not use the skill to fabricate endorsements.

## Reference(s):

- [Wear Everything skill listing](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider setup and data flow](artifact/references/provider-cli.md)
- [Image generation options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown guidance and shell commands; generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates on-model product images saved locally; cloud providers may also return hosted image URLs.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
