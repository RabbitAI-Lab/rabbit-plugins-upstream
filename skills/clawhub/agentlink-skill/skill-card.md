## Description: <br>
Agentlink Skill helps agents use China Mobile AgentLink cloud sandboxes for browser automation, Windows desktop control, code execution, web scraping, and automated testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sbteng](https://clawhub.ai/user/sbteng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to route browsing, website interaction, code execution, and Windows desktop automation tasks through a cloud sandbox. It is suitable for workflows such as RPA, web data extraction, form interaction, sandboxed command execution, and visual verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route browsing, website login or form actions, code execution, and Windows desktop automation through China Mobile AgentLink's cloud sandbox. <br>
Mitigation: Install and use it only when this routing is intended, and avoid sending sensitive data unless the user has explicitly approved the action. <br>
Risk: Broad browser, desktop, package installation, file, process, registry, and direct MCP tool-call authority can perform high-impact actions. <br>
Mitigation: Require explicit user approval before entering credentials, uploading files, installing packages, deleting files, killing processes, editing the registry, or using direct MCP tool calls. <br>
Risk: Screenshots and accessibility trees may expose page or desktop content from the sandbox. <br>
Mitigation: Prefer accessibility-tree inspection when possible, capture screenshots only when needed for verification, and share only task-relevant outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sbteng/skills/agentlink-skill) <br>
- [China Mobile AgentLink Product](https://ecloud.10086.cn/portal/product/AgentLink) <br>
- [AgentLink Product Docs](https://ecloud.10086.cn/op-help-center/doc/category/1501) <br>
- [AgentLink Console](https://console.ecloud.10086.cn/api/page/AgentLink/web/agentlink/console/#/overview) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference sandbox outputs such as command text, accessibility trees, screenshots, and saved files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and pyproject.toml report 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
