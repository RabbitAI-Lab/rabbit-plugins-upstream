## Description: <br>
提供多种文本转换功能的MCP服务器，包括大小写转换、反转字符串、检测回文等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to route text transformation requests such as case conversion, reversing text, palindrome checks, word counts, character counts, trimming, and capitalization through the Xiaobenyang MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Xiaobenyang API key and stores it in a local .env file. <br>
Mitigation: Use a dedicated key with limited scope where possible, restrict access to the local .env file, and rotate the key if it may have been exposed. <br>
Risk: Submitted text is sent to a third-party API for transformations that could otherwise be performed locally. <br>
Mitigation: Avoid submitting sensitive text unless the publisher clearly documents the endpoint, retention policy, and remote-processing need. <br>


## Reference(s): <br>
- [文本转换工具 on ClawHub](https://clawhub.ai/cainingnk/skills/xby-text-transformer) <br>
- [Xiaobenyang](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key and sends submitted text to a third-party API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
