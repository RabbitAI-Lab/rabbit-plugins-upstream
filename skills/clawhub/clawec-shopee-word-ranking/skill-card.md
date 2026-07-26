## Description: <br>
Queries ClawEC's API for Shopee hot-selling and trending keyword rankings by marketplace, category, ranking type, period, and optional list scope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and ecommerce analysts use this skill to retrieve Shopee keyword ranking data from ClawEC and produce Chinese ranking reports with keyword selection recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and the API key are used with ClawEC's external API. <br>
Mitigation: Keep the key in the CLAWEC_API_KEY environment variable, do not hardcode it, and send only keyword-ranking lookups suitable for that provider. <br>
Risk: Ranking reports can be misleading if API errors, pagination, date, or query parameters are not checked. <br>
Mitigation: Check the top-level status, business success flag, error fields, pagination, and query conditions before presenting recommendations. <br>


## Reference(s): <br>
- [Shopee word ranking response schema](references/response-schema.md) <br>
- [ClawEC API base URL](https://www.clawec.com/api) <br>
- [Shopee word ranking API endpoint](https://www.clawec.com/api/aigc/ec/shopee/data/word/ranking) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables, observations, recommendations, and optional shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CLAWEC_API_KEY for authenticated requests; pageSize is capped at 10 by the skill guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
