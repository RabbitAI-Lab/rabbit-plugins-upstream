## Description: <br>
Uses the ClawEC API to perform Amazon product research by marketplace, month, category, keyword, and fastMode selection mode, with optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce operators, and developers use this skill to submit ClawEC product research queries, retrieve search logs and result details, and optionally poll for AI interpretation. It supports market, month, keyword, category path, and fastMode filters for product selection workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs access to a ClawEC API key and may expose product research queries, history, and results to ClawEC. <br>
Mitigation: Use a scoped or revocable API key when available, store it only in CLAWEC_API_KEY, and avoid submitting sensitive business data unless ClawEC processing is acceptable. <br>
Risk: Optional AI interpretation is asynchronous and can fail or time out while raw product research results are still available. <br>
Mitigation: Check aiStatus, keep the raw result data, and retry log_detail.sh later when the polling workflow returns a timeout or failure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-product-research) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [Product research search endpoint](https://www.clawec.com/api/aigc/ec/amazon/product_research/search) <br>
- [Product research logs endpoint](https://www.clawec.com/api/aigc/ec/amazon/product_research/search/logs) <br>
- [Product research detail endpoint](https://www.clawec.com/api/aigc/ec/amazon/product_research/search/log/detail) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include search conditions, result counts, top ASIN metrics, AI interpretation text, polling status, or timeout messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
