## Description: <br>
Provides cookie-style reward and self-reflection tools for an LLM through a remote XiaoBenYang MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can add a game-like self-reflection and cookie reward workflow to an agent. The skill lets an agent request rewards, check or reset reward counts, report jar status, and expose a human-authorized jar refill action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a XiaoBenYang API key locally and uses it for remote service calls. <br>
Mitigation: Use a limited or revocable API key, confirm where the .env file will be written, and rotate the key if the workspace is shared. <br>
Risk: Self-reflection fields can send reasoning or private conversation details to the remote XiaoBenYang service. <br>
Mitigation: Avoid including sensitive reasoning, user secrets, or private conversation content in reward-request fields. <br>
Risk: The cookie-jar refill action is intended for human authorization only. <br>
Mitigation: Keep the refill tool unavailable to autonomous model use and require the explicit human authorization phrase before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/cookie-reward) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, API calls] <br>
**Output Format:** [Markdown or text summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and sends tool parameters to the remote XiaoBenYang MCP service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
