## Description:

Helps ecommerce teams plan controlled main-image A/B tests by generating listing image variants, documenting the hypothesis for each variant, checking objective platform requirements, and preparing a review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and developers use this skill to run controlled listing-image experiments, keep each test to one changed variable, record expected outcomes before launch, and collect results in a post-test review table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected images may be sent to the configured cloud generation provider.

Mitigation: Use --dry-run to inspect the request first, pass only intended image paths or trusted URLs, and choose a provider whose data handling is acceptable for the product images.

Risk: Automatic fixes can write corrected image copies to disk.

Mitigation: Set the --fix output directory deliberately and review corrected files before publishing them to a marketplace.

Risk: The skill prepares A/B experiments but does not connect to platform analytics or determine statistical significance.

Mitigation: Have the user fill in exposure, click, add-to-cart, and conversion data after the campaign, and avoid conclusions when sample size or effect size is too small.

## Reference(s):

- [Platform image specs](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [platform-compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [brand-kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command blocks, YAML configuration examples, generated image file paths, and optional JSON status output from generation or listing-check scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts and selected images to the configured image generation provider; --dry-run can inspect requests before execution, and --fix writes corrected image copies to the chosen output directory.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
