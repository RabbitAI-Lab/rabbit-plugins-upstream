## Description: <br>
Uses the ClawEC API to analyze TikTok Shop products by product ID or product link, including channel mix, content format, paid versus organic traffic, daily trends, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
TikTok Shop sellers, ecommerce analysts, and agent operators use this skill to submit a product ID or link to ClawEC, retrieve product-level performance data, and produce a concise Chinese analysis of sales, GMV, traffic channels, content formats, paid versus organic mix, trends, and optional AI interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product IDs, TikTok Shop product links, regions, and related requests are sent to ClawEC for processing. <br>
Mitigation: Use this skill only with products and account context that are appropriate to process through ClawEC. <br>
Risk: Optional AI interpretation is asynchronous and may fail or time out while the raw product analysis is still available. <br>
Mitigation: Report the AI status clearly, return the available raw analysis data, and retry the detail lookup later when interpretation is still pending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-tiktok-shop-analysis) <br>
- [ClawEC account and API key setup](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [ClawEC TikTok product analysis tool](https://www.clawec.com/tool/tiktok-product-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown summaries, JSON API responses, and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY; optional AI interpretation may be returned after polling.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
