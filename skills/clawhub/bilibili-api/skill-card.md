## Description: <br>
一个为bilibili.com API提供服务的Model Context Protocol (MCP)服务器，支持获取用户信息、视频搜索等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to query Bilibili user profiles, video details, and video search results through configured MCP tool calls. The skill requires a Xiaobenyang API key before making requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence reports that Bilibili-labeled requests are routed through a third-party Xiaobenyang API/proxy. <br>
Mitigation: Use only after reviewing the remote service and supported tool list, and avoid sending sensitive account credentials or private data through the proxy. <br>
Risk: Server security evidence reports that the skill may store the Xiaobenyang API key in a plaintext .env file. <br>
Mitigation: Use a limited or test credential, restrict filesystem access where possible, and rotate or remove the key when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/bilibili-api) <br>
- [Xiaobenyang API key service](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Structured tool results summarized for the user, with raw JSON available from API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY and returns success, raw, and message fields from tool calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
