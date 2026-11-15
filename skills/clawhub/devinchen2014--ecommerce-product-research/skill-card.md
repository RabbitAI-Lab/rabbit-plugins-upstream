## Description:

提供商品类目或已有商品资料，整理电商选品候选清单，列出可见价格、匹配条件、入选理由和待核实事项。预算与受众有则提供；已有资料可直接分析，无需 API Key。在线商品查询支持抖音与小红书。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

电商选品人员和店铺经营者可用已有商品资料，或在抖音、小红书进行有限的在线查询，初筛符合类目、预算和受众条件的商品。技能整理可见价格、匹配理由、来源和待核实事项，供后续人工复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online searches involve third-party data sharing, and search terms could expose confidential keywords or identifiers.

Mitigation: Review the data sharing implications before online search and omit confidential terms or identifiers.

Risk: The CLI uses an unpinned @latest package with automatic approval, creating supply-chain risk if the package changes.

Mitigation: Wait until the CLI release is pinned to a reviewed version before using online CLI queries.

Risk: The security scan was partial and does not establish that the artifact is safe.

Mitigation: Review the source and repeat the security scan when unresolved local references can be analyzed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-research)
- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown candidate table with visible product details, sources, selection reasons, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Online searches are limited to the requested scope and returned data; no market-wide sales or profit claims.]

## Skill Version(s):

0.1.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
