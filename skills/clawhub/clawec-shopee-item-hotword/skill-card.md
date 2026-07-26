## Description: <br>
Queries Shopee item hot search words through the ClawEC API, including search index, recent 30-day sales and GMV, and recommended bid data for traffic keywords or same-category hotwords. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce operators, and agent workflows use this skill to query Shopee hotwords for up to 10 item IDs per request and turn returned metrics into SEO or advertising keyword recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Shopee item IDs and bearer credentials to the ClawEC API. <br>
Mitigation: Use a trusted ClawEC account, prefer a dedicated API key in the CLAWEC_API_KEY environment variable, and avoid hardcoding credentials in prompts or files. <br>
Risk: Hotword recommendations depend on the returned API metrics and request parameters. <br>
Mitigation: Confirm the site, item ID batch, keyword type, and timest value before acting on SEO or advertising recommendations. <br>
Risk: API errors or failed business responses can produce incomplete results. <br>
Mitigation: Check both top-level status and data.success, then surface errorCode or errorMessage before producing recommendations. <br>


## Reference(s): <br>
- [Response Schema](references/response-schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-item-hotword) <br>
- [ClawEC API Endpoint](https://www.clawec.com/api/aigc/ec/shopee/data/item/hotword) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown report with hotword tables, prioritized recommendations, and optional JSON API response details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default report language is Chinese; requests require CLAWEC_API_KEY and support up to 10 item IDs per batch.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
