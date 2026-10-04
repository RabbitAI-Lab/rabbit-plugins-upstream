## Description:

Localizes ecommerce product assets into regional listing copy, size guides, images, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and listing teams use the skill to adapt product copy, sizing information, and listing imagery for different markets and marketplaces. It also flags region-specific labeling considerations for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and referenced images may be sent to a selected cloud generation provider.

Mitigation: Confirm the provider and data-sharing terms before submitting sensitive product assets.

Risk: Generated images, non-English text, and sizing or labeling guidance may not be suitable for a marketplace listing as-is.

Mitigation: Review output files and translations, check current platform rules, and independently confirm sizes and required labels before listing.

Risk: Running an unpinned CLI recovery command could execute an unreviewed package version or write files unexpectedly.

Mitigation: Verify the package source and version; use a dry run or explicit output paths when tighter control is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Shell commands]

**Output Format:** [Localized listing copy and size tables in text or Markdown; generated image files when image generation is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation can save files to a selected path; listing-image checks report platform-specific issues.]

## Skill Version(s):

1.0.14 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
