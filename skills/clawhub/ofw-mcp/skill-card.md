## Description: <br>
Provides guidance for using the ofw-mcp OurFamilyWizard MCP server to access messages, calendar events, expenses, journal entries, drafts, attachments, and account notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need an agent to configure or operate the ofw-mcp MCP server for OurFamilyWizard co-parenting workflows, including reading records and performing controlled write actions. It is intended for users who deliberately want agent-assisted access to sensitive OFW account data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad access to sensitive co-parenting records through a configured OurFamilyWizard account. <br>
Mitigation: Install only when agent access to the account is intentional, and treat credentials plus any local cache as sensitive records. <br>
Risk: Some reads may change visible account state, such as marking a message viewed or updating last-seen status. <br>
Mitigation: Use explicit user confirmation before reads that may mark content viewed, and warn users when preserving unread or unseen status matters. <br>
Risk: Write actions can send messages, delete drafts or events, create expenses, create journal entries, and upload or download attachments. <br>
Mitigation: Require explicit user confirmation before sends, deletes, event changes, expense creation, journal creation, and attachment transfer actions. <br>
Risk: Cached message or draft state can be stale and may not reflect the current server state. <br>
Mitigation: Verify freshness, completeness, and lifecycle status before presenting current OFW state as fact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp) <br>
- [npm package: ofw-mcp](https://www.npmjs.com/package/ofw-mcp) <br>
- [Project source link stated in artifact](https://github.com/chrischall/ofw-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline JSON and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe MCP tool calls and cautions for actions that read or modify OurFamilyWizard records.] <br>

## Skill Version(s): <br>
2.9.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
