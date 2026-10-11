## Description:

Helps cross-border sellers adapt product copy, size charts, listing images, and labeling reminders for different markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and listing teams use this skill to prepare market-specific product copy, size conversions, images, and preliminary platform and labeling checks before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to a configured cloud image-generation provider.

Mitigation: Run a dry-run when possible, select an approved provider, and review its data-handling requirements before sending assets.

Risk: Generated foreign-language image text or localized size conversions may be inaccurate.

Mitigation: Have a native speaker review visible text and confirm size charts against the brand's measurements before publication.

Risk: Automated listing and labeling checks do not establish legal compliance or marketplace approval.

Mitigation: Verify current platform rules and regional labeling requirements through official or qualified channels before listing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Image generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Shell commands, Guidance]

**Output Format:** [Markdown guidance and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-specific copy, size charts, image files, and listing precheck results.]

## Skill Version(s):

1.0.16 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
