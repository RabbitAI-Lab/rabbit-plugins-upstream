## Description:

亚马逊前三页 SERP 市场格局分析专家。适用于分析页面级竞争、自然排名结构、价格分布、评论分布、品牌与卖家集中度、新品机会，并生成 SERP 市场报告的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and analysts use this skill to evaluate the natural results on the first page or first three pages of Amazon SERP data, enrich ASINs with Keepa fields, and produce a market-structure report with JSON and comparison-table outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed LinkFox API, billing, and file-hosting workflows may expose account or report data if a user installs the skill without trusting the provider or points credentials at untrusted hosts.

Mitigation: Install only when LinkFox is trusted, keep gateway and login environment variables pointed at official LinkFox hosts, and avoid uploading private reports unless a public URL is intended.

Risk: Phone/SMS or payment prompts can lead to account or billing actions outside the market-analysis report itself.

Mitigation: Review any phone, SMS, or payment prompt carefully before proceeding.

Risk: The self-extension workflow could add or change skills without an independent security review.

Mitigation: Require separate review and scanning before allowing self-extension to add new skills.

## Reference(s):

- [Amazon search API reference](artifact/skills/linkfox-amazon-search/references/api.md)
- [SERP competition API reference](artifact/skills/linkfox-amazon-search-competition/references/api.md)
- [Keepa field reference](artifact/skills/linkfox-amazon-search-competition/references/keepa-fields.md)
- [Chart templates](artifact/skills/linkfox-amazon-search-competition/references/chart-templates.md)
- [Report analysis layouts](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)
- [AIGC text generation API reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown conversation summary plus generated HTML, JSON, and comparison-table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports disclose sample scope, organic-rank handling, imputed sales values, Keepa coverage, and fallback behavior when enrichment data is unavailable.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
