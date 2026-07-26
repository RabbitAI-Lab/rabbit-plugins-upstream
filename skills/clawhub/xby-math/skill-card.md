## Description: <br>
一个高性能的数学计算协议服务器，提供从基础算术到高级微积分和线性代数的全面数学计算功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to route math, statistics, finance, linear algebra, calculus, and batch calculation requests to the xiaobenyang remote service and return the results in an agent response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends math expressions, datasets, financial scenarios, and batch-operation contents to a remote xiaobenyang service. <br>
Mitigation: Avoid using it for confidential formulas or business data, and use an isolated workspace when evaluating the skill. <br>
Risk: The skill asks for and stores an API key in a local plaintext .env file. <br>
Mitigation: Use a limited-scope API key when possible, protect the workspace, and revoke or rotate the key after testing. <br>
Risk: The public description and tool documentation may make the skill appear more local than it is. <br>
Mitigation: Treat results as remote-service output and review the security guidance before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-math) <br>
- [xiaobenyang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown or plain text summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and sends requested calculations to a remote xiaobenyang API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
