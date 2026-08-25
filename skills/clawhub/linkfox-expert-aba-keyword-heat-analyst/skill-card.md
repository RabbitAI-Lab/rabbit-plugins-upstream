## Description:

专注亚马逊ABA搜索词周维度热度分析，批量拉取多词多周SFR走势对比升温/掉热，支持Top ASIN点击转化份额、同比季节性对比、长尾词回退、关键词扩展与HTML可视化报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts and e-commerce operators use this skill to compare Amazon Brand Analytics weekly Search Frequency Rank trends, validate candidate keywords, inspect optional Top ASIN click and conversion shares, and generate CSV or HTML keyword heat reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon keyword prompts, ASINs, image or media URLs, and product or report files may be sent to external services.

Mitigation: Use the skill only with data approved for those services, avoid private files, and review the configured endpoints before installation.

Risk: File upload paths can create publicly accessible URLs for local reports, CSVs, PDFs, images, or media.

Mitigation: Upload only artifacts intended for public sharing and gate automatic upload behavior in production environments.

Risk: The workflow includes a self-extension path for creating or revising skills.

Mitigation: Remove or require explicit human approval for skill-modification steps before production use.

Risk: Local persistence of generated reports and data can retain business-sensitive keyword or product analysis.

Mitigation: Review output directories, retention expectations, and cleanup procedures for generated files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aba-keyword-heat-analyst)
- [amazon-aba-kw-heat API reference](artifact/skills/amazon-aba-kw-heat/references/api.md)
- [amazon-aba-kw-heat contract](artifact/skills/amazon-aba-kw-heat/references/contract.json)
- [amazon-aba-kw-heat examples](artifact/skills/amazon-aba-kw-heat/references/examples.json)
- [amazon-aba-kw-heat-report layout](artifact/skills/amazon-aba-kw-heat-report/references/layout.json)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown tables with optional CSV download links and HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes SFR trend tables, optional Top ASIN shares, keyword expansion outputs, and year-over-year comparisons; lower SFR means hotter.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
