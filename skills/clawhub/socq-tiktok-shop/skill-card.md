## Description: <br>
Research public TikTok Shop products, shops, creators, categories, and sales signals through SocQ CLI, MCP, or REST workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research teams use this skill to discover and collect public TikTok Shop product, shop, creator, category, review, and sales-signal data while selecting endpoints, estimating credits, running asynchronous tasks, paginating results, and exporting raw files through SocQ. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SocQ requests require an API key and may consume paid credits. <br>
Mitigation: Use environment-based credentials, avoid placing keys in prompts or command history, check account credits before large jobs, and set SocQ account limits. <br>
Risk: Large or retried data collection jobs can duplicate paid submissions or exceed rate and credit limits. <br>
Mitigation: Use reusable idempotency keys for retryable submissions, inspect normalized errors before retrying failed paid requests, and reduce result limits when spend is not authorized. <br>
Risk: TikTok Shop research may be incomplete when pagination stops early, provider failures occur, or requested filters are unsupported. <br>
Mitigation: Report filters, collection time, partial coverage, unsupported filters, provider failures, and final normalized errors with the results. <br>
Risk: The skill is intended for public TikTok Shop data supported by SocQ endpoints. <br>
Mitigation: Collect only public data supported by the selected endpoint and validate inputs against the current endpoint schema. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ TikTok Shop MCP Server](https://api.socq.ai/mcp?platforms=tiktok-shop) <br>
- [TikTok Shop Platform Reference](references/platform.md) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [SocQ TikTok Shop Product API](https://docs.socq.ai/api-manual/tiktok-shop/product) <br>
- [SocQ TikTok Shop Product Reviews API](https://docs.socq.ai/api-manual/tiktok-shop/product-reviews) <br>
- [SocQ TikTok Shop Products API](https://docs.socq.ai/api-manual/tiktok-shop/products) <br>
- [SocQ TikTok Shop Search API](https://docs.socq.ai/api-manual/tiktok-shop/search) <br>
- [SocQ TikTok Shop User Showcase API](https://docs.socq.ai/api-manual/tiktok-shop/user-showcase) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI, MCP, and REST request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, filters, collection times, coverage notes, provider failures, pagination cursors, and raw JSONL export guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
