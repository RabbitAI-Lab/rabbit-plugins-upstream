## Description:

Localizes e-commerce product listings for different markets with adapted copy, size guidance, regional imagery, and platform-checking guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers and listing teams use this skill to adapt product copy, size information, and listing images for target regions and to check image requirements before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation may send product prompts and reference images to an external provider.

Mitigation: Confirm the selected provider with --dry-run or --doctor and do not submit confidential assets unless that provider is approved.

Risk: Automatic image fixes rewrite supplied images as transformed JPEGs.

Mitigation: Review the resulting images before publishing or replacing originals.

Risk: Generated translations, size conversions, and regional labeling hints may be inaccurate.

Mitigation: Have a native speaker review important copy and verify sizes and required labels against brand data and local requirements before listing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Localized copy, Size charts, Guidance, Shell commands, Image files]

**Output Format:** [Text or Markdown guidance and locally saved listing images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image checks report platform-specific issues; generated non-English text and compliance labels need human review.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
