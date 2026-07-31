## Description: <br>
This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, shared expenses, and journal entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to OurFamilyWizard records for co-parenting workflows such as checking messages, managing calendar events, logging expenses, and creating journal entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose or modify sensitive OurFamilyWizard co-parenting records. <br>
Mitigation: Install it only for intended OFW workflows, protect credentials, and limit agent access to users who are allowed to view or change those records. <br>
Risk: Some actions can create durable or visible changes, including sending messages, deleting records, creating expenses or journal entries, uploading files, and changing read or last-seen status. <br>
Mitigation: Require explicit user confirmation before any write action or read action that can update visible OFW status. <br>
Risk: The trigger scope may activate the skill even when the user did not explicitly request OFW access. <br>
Mitigation: Confirm OFW intent before using the skill when the request is ambiguous or only generally relates to co-parenting data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp) <br>
- [npm package: ofw-mcp](https://www.npmjs.com/package/ofw-mcp) <br>
- [Source repository](https://github.com/chrischall/ofw-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or invoke MCP tool calls that read or modify OFW messages, calendar entries, expenses, files, and journal entries.] <br>

## Skill Version(s): <br>
2.9.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
