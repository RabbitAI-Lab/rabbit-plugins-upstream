## Description:

Helps e-commerce teams generate controlled main-image A/B variants, record hypotheses, check listing images, and prepare a results review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to compare product listing main images one variable at a time, document predictions, and review manually supplied click and conversion results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected images may be sent to an external image provider.

Mitigation: Select an approved provider or use dry-run before sending data; avoid confidential or regulated assets unless the provider is approved.

Risk: Generated images or apparent A/B results could mislead buyers or prompt premature publication decisions.

Mitigation: Review images and platform checks before publishing, and fill in real performance data before drawing conclusions.

## Reference(s):

- [ClawHub listing-optimizer release](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image provider usage](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Image files and Markdown experiment hypotheses, checks, and review table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires manual performance data; does not connect to platform analytics or establish statistical significance.]

## Skill Version(s):

1.0.11 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
