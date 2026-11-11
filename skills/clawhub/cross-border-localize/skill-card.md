## Description:

Adapts product assets for cross-border listings with localized copy, regional size conversions, listing visuals, platform-specific image guidance, and compliance-label reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and ecommerce listing teams use this skill to prepare product copy, size charts, listing visuals, and regional platform guidance for selected markets. Users should specify target regions and review translations, platform requirements, and compliance reminders before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious, reporting fail-open image validation behavior and a mismatch between the localization purpose and image checking or editing capabilities; some components were only partially analyzed.

Mitigation: Review the image validation behavior and confirm image checking or editing fits the intended use. Clarify when prompts and images are sent to external providers, and account for the partial scan before installation.

Risk: Generated non-English text may contain errors, size conversions are approximate, and regional compliance reminders are not legal advice.

Mitigation: Have a fluent reviewer check important copy, verify size charts against brand measurements, and confirm applicable labeling requirements with qualified channels before publishing.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow reference](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Ecommerce skills repository](https://github.com/dlazy-ai/ecommerce-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration, Images]

**Output Format:** [Localized listing copy, size conversion tables, regional guidance, shell commands, configuration files, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated non-English text and approximate size conversions need human review; compliance-label guidance is informational.]

## Skill Version(s):

1.0.28 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
