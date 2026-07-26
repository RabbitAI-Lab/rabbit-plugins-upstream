## Description: <br>
Zenrus MCP Server 是一个提供实时货币汇率和石油价格的服务器，支持多种计算功能，适用于金融分析和自动化工具集成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve USD/RUB and EUR/RUB exchange rates, Brent crude oil prices, and simple barrel-purchasing calculations for financial analysis or automation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API-key handling is under-disclosed and the artifact persists XBY_APIKEY in a local .env file. <br>
Mitigation: Only provide a key after review, keep it scoped to this service where possible, and delete or rotate the key when the skill is no longer needed. <br>
Risk: The security summary reports unclear service identity for the upstream API used by the skill. <br>
Mitigation: Verify the XiaoBenYang service and destination domain before sending credentials or financial lookup requests. <br>
Risk: The security verdict is suspicious. <br>
Mitigation: Review and scan the release before installing, and prefer a release that documents credential storage, deletion steps, upstream domains, and pinned patched dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/currency-and-oil) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key before live lookups can be performed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
