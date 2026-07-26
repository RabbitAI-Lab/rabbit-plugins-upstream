## Description: <br>
Queries ClawEC's API for monthly, quarterly, or yearly Shopee shop trend data, including sales, GMV, active rate, follower counts, and optional first-level category filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cross-border ecommerce operators, analysts, and agent developers use this skill to retrieve and interpret Shopee shop trend time series for competitor monitoring and store performance analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Shopee shop IDs, date ranges, and optional category filters to the ClawEC API. <br>
Mitigation: Install only when this data sharing is acceptable for the intended workflow and user environment. <br>
Risk: A ClawEC API key is required to execute requests. <br>
Mitigation: Keep the key in the CLAWEC_API_KEY environment variable and avoid hardcoding or exposing it in prompts, scripts, or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-shop-trend) <br>
- [Publisher profile](https://clawhub.ai/user/anyunzhong) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [Shopee shop trend response schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown report with tables, narrative trend interpretation, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is a Chinese Shopee shop trend report; API requests require site, shop ID, granularity, start date, end date, and optional category and pagination values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
