## Description:

Helps e-commerce sellers create single-variable listing-image A/B tests with hypotheses, image checks, and a review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing managers use this skill to test one main-image change at a time, record hypotheses, and review click-through and conversion results after entering their own platform data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts, reference images, and brand guidance may be sent to the configured image provider.

Mitigation: Confirm the provider and credentials before generation; share only material approved for that provider.

Risk: Example brand defaults may not fit the target market or product policy.

Mitigation: Customize the brand configuration for the product and market before generating variants.

Risk: Generated images may fail current marketplace rules or misrepresent the product.

Mitigation: Review outputs and check against the platform's current requirements before publishing.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Image provider setup and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Guidance]

**Output Format:** [A/B image variants with written hypotheses and a Markdown review table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires users to supply exposure, click, and conversion data; does not determine statistical significance.]

## Skill Version(s):

1.0.15 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
