## Description: <br>
一个基于FastMCP的CSV到JSON转换MCP服务器，提供高效的CSV数据转换服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to inspect CSV file metadata and convert CSV files or CSV strings into JSON through provided tool functions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a third-party xiaobenyang.com API key and persists it in a local plaintext .env file. <br>
Mitigation: Use a dedicated, revocable API key, avoid shared workspaces, and remove the .env entry when the skill is no longer needed. <br>
Risk: CSV content or file references may be sent to a remote service whose endpoint scope, retention, and privacy handling are not clarified in the evidence. <br>
Mitigation: Avoid sensitive CSV data unless the publisher clarifies endpoint behavior, retention, privacy handling, and credential removal. <br>
Risk: ClawHub security evidence marks the release verdict as suspicious because the remote service behavior is not clearly scoped for a simple converter. <br>
Mitigation: Review the skill and ClawHub security guidance before deployment, and test in an isolated environment before using it in normal workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/csv2json) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Configuration] <br>
**Output Format:** [JSON data or status dictionaries, with optional generated JSON file paths and concise text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a xiaobenyang.com API key; CSV content or file references may be sent to a remote service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
