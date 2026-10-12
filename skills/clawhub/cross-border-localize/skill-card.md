## Description:

Helps sellers adapt product listings for regional markets with localized copy, size conversions, image guidance, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and listing teams use this skill to prepare region-specific product copy, sizing information, and marketplace images, then check images against platform requirements before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and supplied reference images are sent to the selected image-generation provider.

Mitigation: Use only approved providers and avoid sensitive local files or internal URLs as reference images.

Risk: Generated non-English text may contain errors.

Mitigation: Have a fluent reviewer check text before publication or add text to a generated text-free image afterward.

Risk: Marketplace image requirements and regional labeling rules vary and may change.

Mitigation: Review current marketplace requirements and confirm required labels with an appropriate specialist before publishing.

Risk: Image checks run with --fix can write adjusted image files.

Mitigation: Use --fix only when you intend to write revised images to the output directory.

## Reference(s):

- [Cross-border Localize release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](references/platform-specs.md)
- [Image generation provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Localized listing copy and sizing guidance in text or Markdown; commands to generate and check marketplace image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files depend on the selected provider and must be checked for marketplace suitability.]

## Skill Version(s):

1.0.17 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
