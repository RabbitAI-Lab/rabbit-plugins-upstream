## Description:

跨境一套素材多区域本地化。一套素材 → 多语言文案、尺码换算表、区域合规标识。当用户说「跨境本地化」「多语言」「翻译上架」「海外版本」「英文版主图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

跨境电商运营人员和商品团队可用此技能为不同市场准备本地化商品文案、尺码对照、区域图片版本及平台规格检查。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to the selected cloud provider, and image generation may incur charges.

Mitigation: Choose the provider explicitly, use --dry-run to review routing, and avoid submitting sensitive material.

Risk: Generated translations, size conversions, image repairs, or regional compliance suggestions may be inaccurate or unsuitable for a listing.

Mitigation: Review repaired images and have translations, sizing, and compliance claims checked before publishing.

Risk: Generated or repaired files may overwrite or mix with existing product assets.

Mitigation: Use a separate output location and inspect the resulting files before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image files, Shell commands, Configuration guidance]

**Output Format:** [Localized listing copy, sizing and platform-check guidance, image files, and CLI JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-specific variants; generated translations, sizing, and compliance notes require review before publishing.]

## Skill Version(s):

1.0.22 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
