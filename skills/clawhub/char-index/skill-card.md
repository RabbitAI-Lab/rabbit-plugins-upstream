## Description: <br>
一个基于字符索引的字符串操作协议服务器，适用于需要精确字符定位的测试代码生成和数据处理场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to perform precise character-index string operations such as finding occurrences, splitting text, inserting or deleting ranges, replacing ranges, matching regex patterns, and extracting substrings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends processed text to a credentialed third-party Xiaobenyang MCP API. <br>
Mitigation: Avoid using the skill with secrets, private code, personal data, or regulated data unless the publisher documents backend, retention, and data-handling practices clearly. <br>
Risk: The skill persists the Xiaobenyang API key in a local .env file. <br>
Mitigation: Install only when local credential storage is acceptable, restrict file access, and rotate the API key if the workspace is shared or exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/char-index) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries of JSON-like tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key before tool calls can return results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
