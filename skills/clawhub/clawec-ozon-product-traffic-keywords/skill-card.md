## Description: <br>
Queries Ozon product traffic keywords through the Clawec API and helps sellers analyze search, conversion, supply-demand, organic, and advertising keyword metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers and operators use this skill to query Ozon product IDs through the Clawec API, interpret traffic keyword metrics, and choose SEO or advertising keywords. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries include Ozon product IDs and keyword filters that are sent to ClawEC. <br>
Mitigation: Use the skill only when sharing those queried identifiers and filters with ClawEC is acceptable. <br>
Risk: The skill requires a CLAWEC_API_KEY for API access. <br>
Mitigation: Keep the API key in an environment variable and do not hard-code it in prompts, scripts, or shared files. <br>


## Reference(s): <br>
- [Ozon product traffic keyword response schema](references/response-schema.md) <br>
- [ClawEC API base URL](https://www.clawec.com/api) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-ozon-product-traffic-keywords) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with tables, keyword recommendations, and optional shell command/API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY. Queries are sent to ClawEC and accept up to 10 Ozon product IDs per request with pageSize up to 15.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
