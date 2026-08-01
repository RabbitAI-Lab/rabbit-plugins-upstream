## Description: <br>
ZooData provides an API endpoint reference and CLI-backed guidance for Amazon commerce and keyword intelligence data, including authentication, endpoint parameters, response fields, credit tracking, and local review analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to understand ZooData API endpoints, configure authentication, choose the right commerce or keyword-intelligence request, and interpret returned fields and credit usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key, and optional plaintext credential files can expose secrets if mishandled. <br>
Mitigation: Prefer the ZOODATA_API_KEY environment variable, avoid unnecessary plaintext credential storage, and remove unintended legacy APICLAW_API_KEY values. <br>
Risk: Broad or repeated workflows can consume ZooData account credits. <br>
Mitigation: Ask for a cost estimate and user confirmation before running multi-call scans. <br>
Risk: Keyword and traffic outputs are directional unless paired with first-party Amazon ABA-SQP conversion evidence. <br>
Mitigation: Label directional conclusions clearly and request ABA-SQP impressions, clicks, cart adds, purchases, click share, purchase share, and conversion rate when conversion quality matters. <br>


## Reference(s): <br>
- [ZooData Skill Page](https://clawhub.ai/apiclaw/skills/zoodata) <br>
- [ZooData GitHub Repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API Docs](https://api.zoodata.ai/api-docs) <br>
- [ZooData OpenAPI Spec](https://zoodata.ai/api/v1/openapi-spec) <br>
- [ZooData API Field Reference](references/reference.md) <br>
- [ZooData OpenAPI Quick Reference](references/openapi-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; live ZooData API calls may consume account credits.] <br>

## Skill Version(s): <br>
1.1.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
