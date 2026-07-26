## Description: <br>
LinkFox Amazon Product Selection helps agents research Amazon product opportunities across competitor lookup, keyword analysis, reviews, niche trends, historical product data, and market opportunity reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and e-commerce researchers use this skill to investigate Amazon product selection, market demand, competitor positioning, keyword traffic, review themes, and niche opportunities. Agents can call the bundled scripts to retrieve LinkFox-backed research data and summarize it for product decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated network calls may send Amazon research queries, ASINs, keywords, uploaded images, and session metadata to the LinkFox gateway. <br>
Mitigation: Use only in approved environments, keep API keys scoped, and avoid sending confidential product plans or sensitive media unless that data sharing is permitted. <br>
Risk: The skill stores full API responses and cache files locally, which may include product research results or user-provided query details. <br>
Mitigation: Run it from an approved workspace, review the generated linkfox output and cache directories, and clean or exclude them before sharing the workspace. <br>
Risk: Artifact documentation references installing an external LinkFox onboarding companion skill. <br>
Mitigation: Do not install or run the companion skill unless it has been separately reviewed and approved. <br>
Risk: Market, keyword, review, and product data may be incomplete, stale, or source-dependent. <br>
Mitigation: Treat outputs as decision support and verify important findings against source marketplaces or approved business data before acting commercially. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-selection) <br>
- [Skill Definition](SKILL.md) <br>
- [Amazon Search Reference](references/linkfox-amazon-search.md) <br>
- [Amazon Product Detail Reference](references/linkfox-amazon-product-detail.md) <br>
- [Amazon Reviews Reference](references/linkfox-amazon-reviews-list.md) <br>
- [Amazon Opportunity Report Reference](references/linkfox-amazon-opportunity-report-by-keyword.md) <br>
- [Keepa Product Request Reference](references/linkfox-keepa-product-request.md) <br>
- [Jungle Scout Product Database Reference](references/linkfox-junglescout-product-database.md) <br>
- [SellerSprite Product Search Reference](references/linkfox-sellersprite-product-search.md) <br>
- [SIF Keyword Overview Reference](references/linkfox-sif-keyword-overview.md) <br>
- [Jiimore Niche Info Reference](references/linkfox-jiimore-get-niche-info-by-keyword.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, shell commands, and JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts can write full API responses and cached results under a local linkfox workspace directory while printing either full JSON or a compact summary.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
