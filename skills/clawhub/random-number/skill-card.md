## Description: <br>
提供伪随机和加密安全的随机数生成功能，包括整数、浮点数、加权选择、列表洗牌和安全令牌生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to request random integers, random floats, weighted choices, shuffled lists, samples, secure hex tokens, and bounded secure random integers through a XiaoBenYang-backed API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a third-party API key and stores it in a plaintext .env file. <br>
Mitigation: Use a dedicated low-privilege API key, avoid sharing the workspace, and rotate or remove the key after use. <br>
Risk: Function inputs and the API key are sent to a third-party remote service. <br>
Mitigation: Do not use the skill with secrets, authentication tokens, sensitive lists, private datasets, or other confidential inputs. <br>
Risk: The security verdict is suspicious because the advertised random-number workflow depends on a remote API client. <br>
Mitigation: Install only when remote XiaoBenYang-backed random-number requests are intentional; prefer a local random generator when remote execution is unnecessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/random-number) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown or text summary of raw JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and sends tool inputs to the remote service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
