## Description:

亚马逊投机型选品专家。适用于寻找短窗口机会、趋势型商品、快速增长商品、高上行空间产品，并需要明确识别风险的选品场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to find short-window, high-sales, multi-seller Amazon product opportunities, review risk signals, export Excel results, optionally score candidate ASINs, and schedule recurring scouting runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses LinkFox credentials and paid account workflows across product search, scoring, text generation, upload, and scheduling features.

Mitigation: Install only in runtimes where those credentials and account actions are intended; use dedicated credentials where possible and review enabled auxiliary skills before use.

Risk: Recurring scouting tasks can repeatedly consume account credits or run unattended workflows.

Mitigation: Confirm cadence and estimated cost before enabling scheduled runs, and periodically list, pause, or delete tasks that are no longer needed.

Risk: File upload behavior can create public URLs for local outputs.

Mitigation: Upload only files that are appropriate for public access and review generated reports, CSVs, PDFs, images, or videos before sharing.

Risk: Bundled behavior includes cross-agent modification capabilities such as patching agent instruction files.

Mitigation: Review proposed instruction-file changes before applying them and keep backups of agent configuration files.

Risk: Product recommendations and ASIN scores are screening aids and may omit deeper risks such as brand concentration, price history, traffic structure, or patent exposure.

Mitigation: Treat results as candidate discovery, then perform additional market, legal, and competitive diligence before commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-opportunistic-product-scout)
- [Main skill definition](artifact/SKILL.md)
- [Product scout API parameter catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [SellerSprite product search API](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [ASIN dynamic scoring expectations example](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File upload API](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown previews, JSON script outputs, and Excel workbooks with product scouting or ASIN scoring results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox credentials and paid-account workflows for API-backed search, scoring, upload, and scheduling features.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
