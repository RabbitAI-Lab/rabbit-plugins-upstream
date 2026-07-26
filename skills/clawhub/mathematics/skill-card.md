## Description: <br>
Provides API-backed mathematical calculation, statistics, matrix operation, unit conversion, number theory, session, and calculation history tools for agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to route mathematical requests to calculation tools for expressions, batches, statistics, matrices, unit conversions, number theory, and session-based work. It is suitable when a workflow can use a remote API-backed calculation service and an API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for and stores XBY_APIKEY locally while sending math queries to a remote service. <br>
Mitigation: Install only when the user trusts xiaobenyang.com, disclose remote processing, and protect or remove the local .env file as appropriate. <br>
Risk: The skill exposes non-math status and memory tools that are broader than its stated calculator purpose. <br>
Mitigation: Review or disable the non-math administrative/status tools when deploying only calculator functionality. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/mathematics) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text summaries of JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; calculation requests are sent to a remote service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
