## Description: <br>
Queries Shopee category trend overviews through the Clawec API, including multi-site monthly, quarterly, or yearly time series for sales, GMV, product, shop, and brand metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cross-border ecommerce sellers, analysts, and agents use this skill to fetch and interpret Shopee category trend data across sites, date ranges, and product or location filters before product selection or market comparison decisions. <br>

### Deployment Geography for Use: <br>
Global, subject to Clawec API availability and Shopee site coverage. <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Clawec API key and sends selected Shopee query parameters to Clawec's external API. <br>
Mitigation: Use the CLAWEC_API_KEY environment variable instead of hardcoding secrets, and confirm the user is comfortable sending the requested parameters to Clawec before execution. <br>
Risk: External API calls can fail because of invalid credentials, unavailable service, or unsupported query parameters. <br>
Mitigation: Check the top-level status, business success flag, error code, and error message before interpreting results. <br>


## Reference(s): <br>
- [Response schema](references/response-schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-category-trend) <br>
- [Clawec API](https://www.clawec.com/api) <br>
- [Clawec API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown report with trend tables and optional bash or curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY and sends selected Shopee sites, category, date range, granularity, product type, and location filters to the Clawec API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
