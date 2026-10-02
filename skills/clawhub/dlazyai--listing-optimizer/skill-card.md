## Description:

Helps e-commerce sellers plan single-variable product-image A/B tests, generate and check image variants, and document hypotheses and results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and their agents use this skill to compare product listing images with one change at a time, record predicted outcomes, and review manually collected performance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected local images may be sent to an image-generation provider.

Mitigation: Use dry-run or select a provider explicitly, and avoid sending sensitive local images.

Risk: Saved image-provider credentials may expose access to a paid account.

Mitigation: Review provider account settings and credential storage before relying on saved CLI credentials.

Risk: Generated images may not satisfy platform listing requirements or accurately represent the product.

Mitigation: Run image checks and review images against current platform rules and the actual product before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image-generation provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Shell commands, Guidance]

**Output Format:** [Generated product-image variants and a Markdown experiment plan and results table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Performance data must be supplied by the user; the skill does not determine statistical significance.]

## Skill Version(s):

1.0.12 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
