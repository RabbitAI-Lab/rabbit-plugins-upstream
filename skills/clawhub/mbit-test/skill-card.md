## Description: <br>
一个用于 MBTI 人格测试的 MCP 服务器，支持 AI 助手引导用户完成人格测试并给出结果分析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers can use this skill to run an MBTI questionnaire through an AI assistant, submit answers, track progress, and summarize the final personality result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the provided API key locally in a plaintext .env file. <br>
Mitigation: Use a limited or revocable API key and remove it from the local .env file when the skill is no longer needed. <br>
Risk: MBTI answers and session state are sent to the XiaoBenYang remote API. <br>
Mitigation: Avoid entering sensitive personal information and review the remote service's data handling expectations before use. <br>
Risk: Stale gaokao-related references make the package scope unclear. <br>
Mitigation: Treat the skill as suspicious until the publisher cleans up unrelated references and confirms the MBTI-only scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/mbit-test) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance, Text] <br>
**Output Format:** [JSON responses summarized as user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key and sends MBTI answers plus session state to the XiaoBenYang remote API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
