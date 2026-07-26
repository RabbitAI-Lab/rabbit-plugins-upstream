## Description: <br>
一个支持多种命理系统（紫微斗数、八字等）的MCP协议服务器，为AI工具提供命理分析与运势查询功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent route fortune-analysis requests to XiaoBenYang API tools for Zi Wei Dou Shu charts, Ba Zi charts, fortune queries, palace analysis, and element-balance analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file as a plaintext secret. <br>
Mitigation: Restrict workspace access, keep .env out of commits and sync tools, and remove the key when it is no longer needed. <br>
Risk: The skill sends sensitive birth-related details, and optionally precise coordinates, to the external XiaoBenYang service. <br>
Mitigation: Use the skill only when users consent to sharing those details with the external service and avoid providing optional location coordinates unless they are necessary. <br>
Risk: Security evidence marks the release as suspicious because privacy framing is not sufficient for the data being sent. <br>
Mitigation: Review the skill before deployment and add user-facing privacy expectations around API-key storage and third-party data sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-mingli) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration] <br>
**Output Format:** [Markdown or structured JSON-derived text returned from API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY secret and may send birth date, birth time, gender, and optional location coordinates to the external XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
