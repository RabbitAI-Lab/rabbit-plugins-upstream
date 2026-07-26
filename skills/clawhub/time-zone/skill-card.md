## Description: <br>
Provides global time-zone management and time conversion for business coordination, travel planning, and developer operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, travelers, and business users use this skill to get current times and convert times between global time zones through the XiaoBenYang MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Timezone requests and the XBY API key are sent to a third-party XiaoBenYang service. <br>
Mitigation: Install only if you trust xiaobenyang.com with the API key and timezone queries; prefer a short-lived or low-privilege key when available. <br>
Risk: The skill stores XBY_APIKEY in a local .env file. <br>
Mitigation: Use a private workspace, keep .env out of commits and shared backups, and rotate the key if it may have been exposed. <br>
Risk: The security evidence reports copied gaokao identifiers that do not match a routine timezone utility. <br>
Mitigation: Review the endpoint, tool IDs, and publisher metadata before routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/time-zone) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration] <br>
**Output Format:** [JSON tool responses summarized as concise user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and sends timezone requests to the XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
