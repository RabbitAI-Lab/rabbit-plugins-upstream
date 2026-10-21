## Description:

Adapts product listings for selected markets with localized copy, size conversions, regional imagery, and marketplace-check guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to prepare region-specific product copy, size charts, listing images, and reminders about marketplace image requirements and local labeling.

### Deployment Geography for Use:

Global; users select target markets for each listing.

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to a cloud generation provider.

Mitigation: Review the dry-run, select an approved provider, and do not send sensitive unreleased assets without authorization.

Risk: Generated translations, model casting, size conversions, or marketplace and labeling guidance may be inaccurate.

Mitigation: Have a fluent reviewer check text and casting, confirm brand-specific measurements, and verify current marketplace and local labeling requirements before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Generation provider and data-flow guide](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Images, Shell commands, Guidance]

**Output Format:** [Localized listing copy and size tables; generated image files and optional JSON image-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-specific image checks and human review are needed before publishing.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
