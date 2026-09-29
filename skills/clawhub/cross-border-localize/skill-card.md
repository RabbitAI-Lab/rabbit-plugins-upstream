## Description:

Helps ecommerce sellers adapt product copy, sizing guidance, listing images, and labeling reminders for different regional markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and listing teams use this skill to prepare region-specific product copy, size comparisons, images, and labeling reminders for cross-border listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation may send prompts and product images to an external AI provider.

Mitigation: Confirm the selected provider and permission to share product assets; use --dry-run or --provider for greater control.

Risk: Generated foreign-language text, size conversions, or labeling suggestions may be inaccurate.

Mitigation: Have a native speaker check important copy, use product-specific centimeter measurements, and confirm labeling requirements before listing.

Risk: Platform image requirements can change and automated checks cannot detect every issue.

Mitigation: Check current platform rules and manually review text, watermarks, and final images before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Image provider usage and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image files, Guidance]

**Output Format:** [Markdown guidance and tables, shell commands, and generated listing images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a configured cloud provider; listing checks cover only machine-checkable image rules.]

## Skill Version(s):

1.0.11 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
