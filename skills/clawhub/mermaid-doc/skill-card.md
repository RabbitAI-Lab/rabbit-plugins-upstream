## Description: <br>
Mermaid Doc MCP Server是一个用于生成Mermaid文档的服务器，提供列出可用图表和检索特定图表文档的功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation authors use this skill to retrieve documentation for Mermaid diagram types and present the returned content to users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary reports a mismatch between the Mermaid documentation claim and XiaoBenYang/Gaokao API credential handling and outbound calls. <br>
Mitigation: Review with the publisher before installation and require a clear explanation of the XiaoBenYang dependency and the exact Mermaid-only operations performed. <br>
Risk: The skill stores XBY_APIKEY in a local .env file and uses it for upstream API calls. <br>
Mitigation: Use a scoped credential, avoid sharing persistent workspaces, rotate the key after testing, and confirm credential storage behavior is acceptable before deployment. <br>
Risk: Outbound requests go to a third-party API service as part of normal operation. <br>
Mitigation: Allow installation only in environments where calls to the documented endpoint are approved and monitored. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/mermaid-doc) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, guidance] <br>
**Output Format:** [Markdown or plain text summarizing returned API data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a diagram_name argument and a configured XBY_APIKEY before upstream calls can succeed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
