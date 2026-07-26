## Description: <br>
一个基于 Python 和 MCP 协议的域名注册状态检查服务器，支持批量检查和双重验证。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and domain operators use this skill to check whether one or more domain names are registered through the XiaoBenYang MCP API and return the API result to the agent user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store the XiaoBenYang API key in a plaintext .env file in the skill working directory. <br>
Mitigation: Prefer providing XBY_APIKEY through a secret manager or environment variable, avoid persisting it when possible, and rotate the key if it has been written to disk. <br>
Risk: Security evidence reports leftover Gaokao and school-search references that do not match the domain-checking purpose. <br>
Mitigation: Review the installed artifact before use and verify the publisher has corrected inconsistent documentation and dependency pinning. <br>
Risk: Using the skill sends domain-check requests and an API credential to the XiaoBenYang upstream service. <br>
Mitigation: Use the skill only when the user accepts the third-party service relationship and understands what data and credential are sent upstream. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/fastdomaincheck) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a domains array and an XBY_APIKEY credential for upstream API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
