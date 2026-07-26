## Description: <br>
Inspect Mermail API and email usage and manage workspaces, members, invitations, email domains, mailboxes, and storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Workspace administrators and developers use this skill to inspect Mermail usage and manage workspace members, invitations, email domains, mailboxes, storage, plan usage, RPM, and credits while preserving the API key's workspace boundary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can administer real Mermail workspace resources when given API-key access. <br>
Mitigation: Use an API key scoped to the intended workspace, review previews carefully, and verify affected resources after changes. <br>
Risk: Member, domain, mailbox, and deletion actions can change access, routing, ownership, or stored data. <br>
Mitigation: Require explicit approval for invitations and destructive changes, and use the single-use destructive-action token flow before deletion or member removal. <br>


## Reference(s): <br>
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills) <br>
- [Workspace administration tool map](references/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Markdown guidance with MCP tool-call and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and the Mermail MCP server; administrative writes require previews and approval.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
