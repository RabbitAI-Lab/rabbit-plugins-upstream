## Description: <br>
Provides agent access to OurFamilyWizard co-parenting messages, calendar events, shared expenses, and journal entries through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to their OurFamilyWizard account, review co-parenting records, and perform message, calendar, expense, and journal workflows with appropriate confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant an agent broad access to sensitive OurFamilyWizard co-parenting records. <br>
Mitigation: Install only when agent access to the OFW account is intended, use explicit OFW requests, and avoid background checks. <br>
Risk: Cached OFW data can be stale while still appearing usable. <br>
Mitigation: Check the provided freshness signals before relying on cached messages, drafts, or other OFW state. <br>
Risk: Some operations can write, upload, send, delete, or change read and last-seen status in a legal-family record system. <br>
Mitigation: Require user confirmation before writes, uploads, sends, deletes, or status-changing reads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp) <br>
- [npm package](https://www.npmjs.com/package/ofw-mcp) <br>
- [Source repository](https://github.com/chrischall/ofw-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON and shell command examples; MCP tool results may include text and structured data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May access or modify OFW records through MCP tools; cached read results include freshness signals that should be checked before relying on current state.] <br>

## Skill Version(s): <br>
2.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
