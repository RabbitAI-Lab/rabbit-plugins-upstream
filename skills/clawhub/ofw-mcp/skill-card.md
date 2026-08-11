## Description:

This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when they need to read, draft, send, or update OurFamilyWizard co-parenting records through the ofw-mcp toolset. It is intended for sensitive family-record workflows where message state, draft freshness, and explicit confirmation matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change sensitive co-parenting records in OurFamilyWizard.

Mitigation: Install only when this account access is intended, use the narrowest available configuration, and require explicit confirmation before sends, deletes, calendar changes, expenses, or journal writes.

Risk: Broad automatic activation could expose private family-record workflows to unintended agent actions.

Mitigation: Keep activation scoped to explicit OurFamilyWizard requests and avoid background actions that read messages, update last-seen status, or modify records.

Risk: Account credentials may be exposed if stored in shared project or user configuration.

Mitigation: Store OFW credentials only in appropriately restricted local configuration or secret storage, not broadly shared workspace files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp)
- [npm package listed by the skill](https://www.npmjs.com/package/ofw-mcp)
- [GitHub repository listed by the skill](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agent calls that read or modify OurFamilyWizard records; user confirmation is expected for sensitive write operations.]

## Skill Version(s):

2.10.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
