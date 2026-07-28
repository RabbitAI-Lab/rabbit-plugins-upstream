## Description: <br>
Provides an API reference and local CLI workflows for ZooData commerce and keyword-intelligence endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to understand and call ZooData endpoints for Amazon commerce, product, review, market, and keyword-intelligence data. It is intended for authenticated, credit-consuming API workflows that need exact endpoint names, request parameters, response fields, and operational caveats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact includes a bundled ZooData API key and expects authenticated API access. <br>
Mitigation: Remove or rotate the bundled key before use and configure ZOODATA_API_KEY through a safer secret path. <br>
Risk: Broad or ambiguous workflows can make many paid ZooData API calls and consume account credits. <br>
Mitigation: Require explicit confirmation for broad multi-call scans and state estimated credit usage before running them. <br>
Risk: API calls can send product identifiers, keywords, categories, dates, numeric filters, and raw review text to ZooData. <br>
Mitigation: Use the skill only when live ZooData calls are intended and avoid submitting unnecessary sensitive or user-profile text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/zoodata) <br>
- [Publisher metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData live OpenAPI specification](https://zoodata.ai/api/v1/openapi-spec) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may invoke credit-consuming authenticated ZooData API calls.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
