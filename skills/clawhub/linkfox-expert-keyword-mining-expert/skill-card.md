## Description:

亚马逊关键词挖掘与扩展专家，适用于关键词发现、种子词扩展、流量词挖掘、反查 ASIN 关键词、搜索词筛选，以及为亚马逊选品研究生成关键词列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace analysts, and ecommerce operators use this skill to mine high-value keywords from ASINs, reviews, SIF, ABA, SellerSprite, and Amazon search suggestions. It helps produce tagged keyword libraries, positive and negative keyword splits, root-frequency analysis, and keyword guidance for Listing optimization and PPC workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send ASINs, reviews, prompts, generated reports, and API-key-backed requests to LinkFox or Amazon-related endpoints.

Mitigation: Install only for LinkFox cloud workflows, avoid sensitive inputs, and keep LinkFox gateway environment variables pointed at trusted hosts.

Risk: The artifact bundles broader upload, scheduling, and skill-creation capabilities beyond keyword mining.

Mitigation: Review requested actions before approving uploads, recurring tasks, or skill-creation changes, and limit use to the capabilities needed for the current analysis.

Risk: Public uploads may expose generated files or data intended to stay private.

Mitigation: Check report and file contents before approving upload or sharing flows.

Risk: Recurring tasks can persist beyond a single keyword analysis session.

Mitigation: Confirm schedule, notification targets, and stop conditions before creating or modifying tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-keyword-mining-expert)
- [Root skill definition](artifact/SKILL.md)
- [SIF ASIN keyword API reference](artifact/skills/linkfox-sif-asin-keywords/references/api.md)
- [ABA intelligent query API reference](artifact/skills/linkfox-aba-intelligent-query/references/api.md)
- [SellerSprite traffic keyword API reference](artifact/skills/linkfox-sellersprite-traffic-keyword/references/api.md)
- [Amazon reviews API reference](artifact/skills/linkfox-amazon-reviews-list/references/api.md)
- [Amazon keyword library taxonomy details](artifact/skills/amazon-keyword-library-builder/references/taxonomy-details.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown summaries and generated HTML report files with structured keyword tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use LinkFox cloud services and Amazon-related data sources; generated reports, public uploads, or scheduled tasks can persist when those bundled capabilities are invoked.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
