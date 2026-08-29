## Description:

上架前平台合规校验与自动修复：检查待上架图片在 Amazon, TikTok Shop, Temu, Shopee, 淘宝等平台的通过或驳回风险，并可修复部分几何与色彩规格问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and listing teams use this skill to check product images against platform-specific image requirements before upload. It reports objective compliance issues such as background color, image size, subject occupancy, transparency, border, file format, file size, and color mode, and can generate corrected image files for supported geometry and color issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled generation and provider scripts can upload prompts or product images to third-party services and may use local API credentials.

Mitigation: Use scripts/check_listing.py for the documented local compliance workflow, and review or remove generation/provider scripts before installation when cloud upload is not acceptable.

Risk: The checker covers machine-testable image constraints and does not judge text, watermarks, collages, or whether platform rules have changed.

Mitigation: Confirm current platform requirements, override rules with --rules when needed, and route content-level checks to a visual model or human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, files, guidance]

**Output Format:** [CLI text reports or JSON, with optional corrected JPEG files when --fix is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 indicates pass, 1 indicates reject risk, and 2 indicates argument or image-read errors.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
