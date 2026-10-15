## Description:

Creates single-variable A/B variants of ecommerce listing images with test hypotheses, image checks, and a results-review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketing teams use this skill to compare one change at a time in listing images, document expected outcomes, check image requirements, and record campaign results for later review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to the selected image-generation provider.

Mitigation: Check the selected provider in dry-run or doctor mode and share sensitive or unreleased assets only when the provider arrangement permits it.

Risk: Generation and image repair can process files and save results under user-directed commands.

Mitigation: Run commands only on files and output locations you intend to process.

Risk: Platform image rules may change, and small samples can make apparent A/B winners unreliable.

Mitigation: Confirm current platform requirements and gather adequate campaign data before deciding which variant performs better.

## Reference(s):

- [Listing Optimizer release on ClawHub](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Image generation provider setup](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Generated image files and a Markdown A/B hypothesis and review table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The review table requires the user to add actual impressions, clicks, and conversions; image checks do not guarantee marketplace acceptance.]

## Skill Version(s):

1.0.17 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
