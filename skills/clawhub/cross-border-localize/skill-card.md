## Description:

Adapts e-commerce product materials into region-specific listing copy, size charts, images, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to adapt product copy, size information, and marketplace images for target regions and to identify labels requiring review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and supplied images may be shared with the selected generation provider.

Mitigation: Use dry-run or doctor modes first, supply only trusted image sources, and avoid confidential launch assets unless provider terms permit sharing.

Risk: Generated non-English copy, size conversions, and compliance labels may be inaccurate or unsuitable for the target marketplace.

Mitigation: Have a fluent reviewer check localized text, verify dimensions against the product's measurements, and confirm labeling and platform requirements before listing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Generation provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Shell commands, Guidance]

**Output Format:** [Localized listing copy and size tables in Markdown; generated image files and listing-check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a configured third-party provider; listings require human review.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
