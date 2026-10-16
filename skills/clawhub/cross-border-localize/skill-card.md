## Description:

Adapts e-commerce product assets for regional markets with localized copy, size conversions, listing images, and compliance-label guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to adapt product copy, sizing information, and imagery for selected regions and marketplaces. It provides platform checks and compliance-label reminders, not legal advice or guaranteed translation accuracy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected images are processed by the configured generation provider.

Mitigation: Use --dry-run for sensitive work and select an approved provider before sending assets.

Risk: Generated foreign-language text and size conversions may be inaccurate.

Mitigation: Have a fluent reviewer check copy and text overlays; verify sizes against the brand's measurements in centimeters.

Risk: Marketplace requirements and regional compliance markings may be incomplete or change.

Mitigation: Check each listing against current platform requirements and confirm required labels through appropriate channels before publishing.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Images, Shell commands, Guidance]

**Output Format:** [Localized copy and size tables in text or Markdown; generated image files and marketplace-check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image files are saved to user-selected paths; outputs depend on the selected region, platform, and generation provider.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
