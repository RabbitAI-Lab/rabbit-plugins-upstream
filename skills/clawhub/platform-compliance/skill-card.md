## Description:

上架前平台合规校验与自动修复：针对待上架图片生成 Amazon、TikTok Shop、Temu、Shopee、淘宝的通过或驳回风险报告，并可一键修成合规图；适用于用户询问是否会被驳回、合规检查、白底或主图规格等场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and catalog teams use the skill to check product listing images against marketplace specifications and save corrected copies for supported geometry and color issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image-generation providers may receive prompt text and uploaded product images.

Mitigation: Use a provider approved for the data involved, and avoid sending sensitive or unapproved images.

Risk: An unpinned CLI command can change behavior between runs.

Mitigation: Review and pin the CLI version before using it in automated or production workflows.

Risk: Marketplace image rules can change, making built-in checks outdated.

Mitigation: Check current official marketplace guidance and update thresholds through the custom rules option when needed.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands, Files]

**Output Format:** [Marketplace compliance reports, shell commands, and optionally repaired image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can check batches and emit JSON; repaired images are saved to a separate output directory.]

## Skill Version(s):

1.0.30 (source: SKILL.md frontmatter; server release 1.0.30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
