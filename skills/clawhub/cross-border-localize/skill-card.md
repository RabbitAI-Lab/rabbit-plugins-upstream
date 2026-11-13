## Description:

跨境一套素材多区域本地化。一套素材 → 多语言文案、尺码换算表、区域合规标识。当用户说「跨境本地化」「多语言」「翻译上架」「海外版本」「英文版主图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and ecommerce teams use the skill to adapt product copy, size information, imagery, and listing guidance for selected regions and marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded product images may be sent to the selected external image provider.

Mitigation: Choose a provider deliberately and upload only images approved for that service.

Risk: The security evidence reports unclear behavior and tool scope, a broad trigger, and partial scan coverage (60% of components fully scanned).

Mitigation: Review the skill's requested actions and external services, and assess the uncovered files before enabling it.

Risk: Generated non-English text can be inaccurate, and the sample size conversions are only indicative.

Mitigation: Have a fluent speaker check localized copy and verify measurements against the product's brand-specific size chart.

Risk: Regional compliance prompts may not cover every requirement and are not legal advice.

Mitigation: Confirm current requirements for each destination market with authoritative sources or qualified professionals before listing.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Image provider CLI and data flow](references/provider-cli.md)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image files, Guidance, Shell commands]

**Output Format:** [Localized product copy and size tables, generated images, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected region and platform; generated foreign-language text, size conversions, and compliance prompts require review.]

## Skill Version(s):

1.0.29 (source: SKILL.md frontmatter; server release 1.0.29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
