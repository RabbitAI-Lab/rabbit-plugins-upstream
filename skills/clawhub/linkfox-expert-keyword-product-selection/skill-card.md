## Description:

围绕种子词或给定关键词完成亚马逊关键词选品全流程，使用 Amazon 搜索与卖家精灵供需比筛选细分市场，补充代表商品后按需供比输出候选清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace sellers and analysts use this skill to expand or validate product keywords, screen niches with demand and competition signals, enrich representative product data, and produce a ranked candidate list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requires LinkFox API credentials and calls external LinkFox and Amazon-related services.

Mitigation: Install only in environments intended for those services, provide the least-privileged credentials available, and review intended calls before running workflows that consume credits or submit data.

Risk: The package can write session data under LinkFox directories.

Mitigation: Run it in a controlled workspace and review generated files before sharing or retaining them.

Risk: The bundle includes public file-upload, AIGC, automatic feedback, and remote onboarding-install behaviors that may not be needed for every deployment.

Mitigation: Review these bundled capabilities before installation and disable or remove them when they are outside the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-keyword-product-selection)
- [Package skill definition](artifact/SKILL.md)
- [Keyword selection method](artifact/skills/keyword-selection-method/SKILL.md)
- [Step S1 candidate keyword retrieval](artifact/skills/keyword-selection-method/references/steps/S1.md)
- [Step S2 representative ASIN and demand-supply screening](artifact/skills/keyword-selection-method/references/steps/S2.md)
- [Step S3 representative product enrichment](artifact/skills/keyword-selection-method/references/steps/S3.md)
- [Step S4 ranked output assembly](artifact/skills/keyword-selection-method/references/steps/S4.md)
- [Amazon search API reference](artifact/skills/linkfox-amazon-search/references/api.md)
- [SellerSprite traffic keyword API reference](artifact/skills/linkfox-sellersprite-traffic-keyword/references/api.md)
- [Keepa product request API reference](artifact/skills/linkfox-keepa-product-request/references/api.md)
- [Report layout reference](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown summaries and ranked JSON-style keyword/product selection data, with optional HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long narrative reports are written to files when the skill's own workflow requires it.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
