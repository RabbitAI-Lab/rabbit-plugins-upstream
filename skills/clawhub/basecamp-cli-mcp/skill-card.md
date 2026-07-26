## Description: <br>
CLI and MCP server for Basecamp 4 that lets agents interact with projects, todos, messages, schedules, kanban cards, documents, campfires, and related project-management workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drkraft](https://clawhub.ai/user/drkraft) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to connect an AI assistant to Basecamp 4 through a CLI or MCP server, enabling project management actions such as listing projects, managing todos, posting messages, updating schedules, and creating webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an AI assistant change or delete Basecamp data. <br>
Mitigation: Use a least-privilege Basecamp OAuth app or account, and test workflows in a non-production Basecamp project before using them on live data. <br>
Risk: Webhook tools can create outbound integrations to external URLs. <br>
Mitigation: Review each webhook URL and disable webhook creation in unattended workflows unless that action is expected. <br>
Risk: The release was flagged as suspicious by the authoritative ClawHub security evidence. <br>
Mitigation: Install only when the publisher is trusted and the intended workflow requires assistant access to real Basecamp data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drkraft/skills/basecamp-cli-mcp) <br>
- [Basecamp CLI Repository](https://github.com/drkraft/basecamp-cli) <br>
- [npm Package: @drkraft/basecamp-cli](https://www.npmjs.com/package/@drkraft/basecamp-cli) <br>
- [Basecamp API Reference](https://github.com/basecamp/bc3-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke Basecamp API actions through CLI commands or MCP tools when configured with OAuth credentials.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
