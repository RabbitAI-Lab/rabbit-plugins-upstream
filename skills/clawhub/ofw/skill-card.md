## Description:

This skill helps agents work with OurFamilyWizard co-parenting data, including messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to access and manage OurFamilyWizard co-parenting records, including inbox review, draft handling, calendar updates, shared expenses, and journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad read and write access to sensitive OurFamilyWizard co-parenting records.

Mitigation: Install only when an agent should access the account, protect credentials and local caches or downloads, and use the narrowest available configuration.

Risk: Messages, deletions, expenses, journal entries, and calendar changes can affect legal or family records.

Mitigation: Require explicit user confirmation before sending messages, deleting records, creating expenses, or making journal and calendar changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [npm package: ofw-mcp](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents through read and write actions against sensitive co-parenting records; user confirmation is needed for irreversible or record-changing operations.]

## Skill Version(s):

2.19.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
