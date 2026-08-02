## Description: <br>
Provides agent access to OurFamilyWizard co-parenting messages, calendar events, expenses, journal entries, and related account information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and manage OurFamilyWizard co-parenting records, including messages, calendars, expenses, journals, drafts, attachments, and account notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access highly sensitive co-parenting records and uses account credentials. <br>
Mitigation: Install only when OFW account access is intended, prefer a local setup unless the hosted connector's operator and logging practices are understood, and avoid using it for generic co-parenting questions. <br>
Risk: Write, delete, send, mark-read, and status-changing actions can have visible or irreversible effects in OurFamilyWizard. <br>
Mitigation: Require explicit user confirmation before any write, delete, send, mark-read, or other status-changing action. <br>
Risk: Cached message or draft state may be stale and can mislead the agent about the current OFW state. <br>
Mitigation: Use live freshness, status, and completeness checks before stating current state or final counts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp) <br>
- [npm package listed by skill artifact](https://www.npmjs.com/package/ofw-mcp) <br>
- [Source link listed by skill artifact](https://github.com/chrischall/ofw-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with command, JSON configuration, and tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP tool calls that read or modify OurFamilyWizard account data.] <br>

## Skill Version(s): <br>
2.10.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
