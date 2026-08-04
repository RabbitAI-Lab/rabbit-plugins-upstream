## Description: <br>
Supports Shopee cross-border ecommerce analysis using Shopdora OpenAPI workflows for keyword research, product discovery, review analysis, category browsing, and balance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fionavv](https://clawhub.ai/user/fionavv) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce operators, analysts, and developers use this skill to query Shopee market data through Shopdora for product selection, keyword research, competitor analysis, review analysis, category lookup, and paid-account quota checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid Shopdora credentials and reusable access tokens are stored under ~/.shopdora in plaintext. <br>
Mitigation: Use least-privilege API credentials, restrict ~/.shopdora file permissions, avoid shared machines, and rotate client secrets or tokens if exposed. <br>
Risk: Cached API results can include review data and are stored locally for 24 hours. <br>
Mitigation: Clear cached review data when it is no longer needed and avoid collecting or exporting personal review data without a valid business need and legal basis. <br>
Risk: Keyword, product, and review endpoints consume paid quota when successful non-empty results are returned. <br>
Mitigation: Confirm site, filters, pagination, and other paid-call parameters with the user before execution and show quota impact for additional retrieval. <br>


## Reference(s): <br>
- [Shopdora OpenAPI Reference](artifact/references/api_docs.md) <br>
- [Shopdora Website](https://www.shopdora.com) <br>
- [Shopdora OpenAPI Base](https://openapi.shopdora.cn/openapi/) <br>
- [ClawHub Skill Page](https://clawhub.ai/fionavv/skills/shopdora-shopee-tool) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, API request examples, and structured tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-facing confirmations before paid calls, structured result summaries, local cache guidance, and quota-aware status messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
