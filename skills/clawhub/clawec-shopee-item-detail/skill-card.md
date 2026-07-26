## Description: <br>
This skill helps an agent query the ClawEC API for Shopee item details and operating metrics, including price, daily/weekly/monthly sales, GMV, ratings, and comments for up to 10 item IDs at a time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commerce operators, analysts, and agent builders use this skill to retrieve Shopee product detail data by site and item ID, then summarize individual products or compare products for SKU research and competitor analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Shopee item IDs, site/date parameters, and a ClawEC API key to the disclosed ClawEC API. <br>
Mitigation: Use the CLAWEC_API_KEY environment variable, prefer a dedicated API key when possible, and avoid pasting unrelated secrets. <br>
Risk: API calls can fail or return business-level errors when the API key, site, item IDs, or date parameter are invalid. <br>
Mitigation: Check the top-level status and data.success fields, then report errorCode and errorMessage with guidance to verify the key, site, and itemIds. <br>


## Reference(s): <br>
- [Response schema](references/response-schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-item-detail) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with optional shell commands and JSON API response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is a concise Chinese report covering query conditions, product basics, sales performance, and two to three actionable observations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
