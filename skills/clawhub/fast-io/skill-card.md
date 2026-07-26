## Description: <br>
Fast.io guides agents through authenticated MCP workflows for shared workspaces, file storage and sharing, document AI, workflow tracking, approvals, and human handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dbalve](https://clawhub.ai/user/dbalve) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to connect agents to Fast.io workspaces, manage files and shares, coordinate tasks and approvals, and hand completed workspace ownership to humans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give agents broad authenticated control over Fast.io workspaces, files, shares, members, API keys, billing-adjacent operations, and raw API execution. <br>
Mitigation: Use scoped, expiring, read-only or entity-limited credentials where possible, and require explicit human approval before billing changes, API key changes, ownership transfer, account or organization closure, purge/delete operations, or mutating execute calls. <br>
Risk: Public QuickShares and share links can expose files outside the authenticated workspace boundary. <br>
Mitigation: Review every public QuickShare or share configuration before distributing links, and avoid sharing sensitive files unless access level, password, and expiration settings are appropriate. <br>
Risk: The artifact includes workflows that run upload curl commands and call raw API endpoints through execute. <br>
Mitigation: Inspect generated shell commands and raw API paths before execution, prefer documented MCP tools, and avoid curl-to-shell installer patterns. <br>


## Reference(s): <br>
- [Fast.io homepage](https://fast.io) <br>
- [Fast.io REST API reference](https://api.fast.io/llms.txt) <br>
- [Fast.io platform guide](references/REFERENCE.md) <br>
- [ClawHub skill page](https://clawhub.ai/dbalve/skills/fast-io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with MCP tool calls, JSON parameters, URLs, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and authenticated Fast.io MCP sessions for most operations.] <br>

## Skill Version(s): <br>
1.233.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
