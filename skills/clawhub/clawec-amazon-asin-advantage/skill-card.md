## Description: <br>
Analyzes Amazon ASIN advantage through the ClawEC API, including ASIN details, sales trends, sales forecasts, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon marketplace operators and ecommerce analysts use this skill to request ClawEC ASIN advantage analysis for a marketplace, ASIN, and optional month. It helps agents return product details, sales trend data, sales forecasts, and optional AI interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an API key to call an external ClawEC API. <br>
Mitigation: Read the key from CLAWEC_API_KEY or ask the user for it at runtime; do not hard-code or expose the key in generated commands, logs, or saved files. <br>
Risk: ASIN analysis requests may consume ClawEC account credits or points. <br>
Mitigation: Confirm the ASIN, marketplace, month, selected analysis options, and returned pointInfo before treating a run as complete. <br>
Risk: Optional AI interpretation is asynchronous and can fail or time out. <br>
Mitigation: Poll log detail within the documented attempt limit, return raw analysis data when interpretation fails, and tell the user when the interpretation is still pending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-asin-advantage) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [ASIN advantage search endpoint](https://www.clawec.com/api/aigc/ec/amazon/asin_advantage/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ASIN details, sales trend tables, forecast data, AI analysis text, status fields, and point-consumption metadata from the ClawEC API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
