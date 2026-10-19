## Description:

检查电商商品图的平台规格并生成驳回风险报告，可按需导出修正后的图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员与开发者用于在上架前检查 Amazon、TikTok Shop、Temu、Shopee、Shopify 和淘宝的商品图片，并修复可机检的规格问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included generation path can send prompts and images to a cloud provider, use provider credentials, incur charges, and write output files.

Mitigation: Use the local inspection and --fix command for compliance checks; run cloud generation only with informed consent about the provider, data sharing, cost, and output destination.

Risk: A passing pixel-based check may miss text, watermarks, or defective product imagery.

Mitigation: Review image content separately before listing; treat the inspection result as a check of measurable specifications only.

Risk: Built-in platform thresholds may become outdated or differ by listing type.

Mitigation: Confirm the current requirements for the target platform and listing type, and override thresholds with custom rules when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Plain-text or JSON inspection report; optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch checks; corrected files are saved separately; exit status indicates rejection risk.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
