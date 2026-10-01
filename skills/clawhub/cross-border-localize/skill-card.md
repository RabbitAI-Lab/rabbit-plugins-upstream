## Description:

Helps sellers adapt product listings for different markets with localized copy, size guidance, region-specific images, and platform checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to prepare market-specific product copy, size charts, and listing imagery, then check images against selected marketplace specifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be shared with the configured AI provider.

Mitigation: Use dry-run or doctor mode to inspect the selected provider before submitting sensitive material.

Risk: Generated non-English text and size conversions may be inaccurate.

Mitigation: Have a fluent reviewer check localized copy and verify measurements against the brand's size chart.

Risk: Image checks do not establish current marketplace or legal compliance.

Mitigation: Confirm current platform requirements and required labeling independently before publishing.

Risk: Automatic image fixes can create derived image files.

Mitigation: Run --fix only when edited copies are intended, and inspect them before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Image generation provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Images]

**Output Format:** [Localized listing copy and size guidance in text or Markdown; generated image files and image-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation uses a configured AI provider; listing checks can report results as text or JSON.]

## Skill Version(s):

1.0.12 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
