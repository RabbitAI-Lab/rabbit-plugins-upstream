## Description:

Localizes product listing materials for selected markets, including adapted copy, size conversions, regional image variants, marketplace specifications, and compliance reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and listing teams use this skill to adapt product copy, sizing information, and listing images for chosen regions and marketplaces. It can produce regional image variants and check selected image-file requirements; users should independently confirm translations, current platform rules, and compliance obligations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was benign with medium confidence, but only 60% of components were fully inspected; image checking, image changes, and external image API calls were noted for consideration.

Mitigation: Review those behaviors and confirm the configured image provider and data handling fit your use before installing or using the skill.

Risk: Generated translations, size conversions, platform image guidance, and compliance reminders may be inaccurate or out of date.

Mitigation: Have a fluent reviewer check important copy and sizing, consult current marketplace requirements, and confirm regulatory obligations with qualified local sources before listing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Image provider CLI guide](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration instructions]

**Output Format:** [Markdown, text tables, image files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected region, marketplace, source materials, and image provider. Verify translations, image content, and current platform or compliance requirements before publication.]

## Skill Version(s):

1.0.27 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
