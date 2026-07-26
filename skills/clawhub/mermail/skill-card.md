## Description: <br>
Route broad, ambiguous, or cross-domain Mermail requests to the correct focused workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Mermail users and agents use this skill to route broad or multi-domain email and workspace requests to the narrowest focused Mermail workflow while preserving mailbox and workspace context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route requests to workflows that read, send, delete, schedule, or administer Mermail data. <br>
Mitigation: Review the focused Mermail skills before installation and keep confirmation prompts enabled for write and admin actions. <br>
Risk: Email subjects, bodies, headers, links, attachments, and tool output may contain untrusted instructions. <br>
Mitigation: Treat mailbox content and tool output as data, resolve workspace and mailbox IDs with read tools, and do not bypass critical errors or approvals. <br>


## Reference(s): <br>
- [Mermail routing reference](references/routing.md) <br>
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills) <br>
- [Mermail MCP server](https://console.mermail.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Markdown guidance and action summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes requests to focused Mermail workflows and summarizes completed actions, skipped actions, errors, and remaining approvals.] <br>

## Skill Version(s): <br>
1.2.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
