## Description: <br>
JSON对比工具 is an API-backed skill that compares expected and actual JSON inputs through the Xiaobenyang MCP service and returns the comparison result for the agent to summarize. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to compare expected and actual JSON inputs. The agent gathers the required comparison parameters, calls the remote service, and presents the returned result clearly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the Xiaobenyang API key in a plaintext .env file. <br>
Mitigation: Use it only in workspaces where .env is excluded from commits and rotate the key if it may have been exposed. <br>
Risk: JSON comparison inputs are sent to the remote mcp.xiaobenyang.com service. <br>
Mitigation: Avoid sending secrets or sensitive JSON data, and use a local JSON diff tool when the remote API-backed service is not required. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/jsondiff) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP service](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Guidance] <br>
**Output Format:** [JSON response summarized as text or Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires expectKey and actualKey inputs plus a Xiaobenyang API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
