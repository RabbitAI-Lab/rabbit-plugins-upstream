## Description:

小红书选品 / 商品趋势分析（product trend analysis）——发笔记前先看商品在小红书有没有热度：传入商品图片，自动判断品类/风格/场景方向，搜近 2 周热度趋势，深挖真实爆款笔记（赞≥100）做分维度拆解，输出宣传方向 + 爆款素材 HTML 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and operators use this skill before posting a product on Xiaohongshu/XHS to estimate trend fit, identify a promotion direction, and review comparable high-performing notes. It is intended for product promotion planning that needs concrete heat signals and reference material before drafting a post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates a Chrome session that may already be logged in to XHS.

Mitigation: Run it only with an account and browser profile appropriate for automation, and review XHS session exposure before execution.

Risk: Product descriptions, note data, and prompt context are sent to the configured LLM endpoint.

Mitigation: Keep WC3_LLM_ENDPOINT pointed at a trusted local service or another endpoint approved for the data being processed.

Risk: A local product_image path may be read and embedded into the generated report.

Mitigation: Do not pass sensitive local file paths as product_image, and use a dedicated non-sensitive product image file.

Risk: The helper file wc3-code.mjs is obfuscated and has under-disclosed data-flow behavior.

Mitigation: Review, replace, or deobfuscate the helper before using the release in a sensitive environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fatmind/skills/xhs-product-trend-fit)
- [webclaw3 browser automation runtime](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [HTML report with JSON result metadata and Markdown data details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes an HTML report, res.json, and data.md to the configured output directory.]

## Skill Version(s):

1.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
