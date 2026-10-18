## Description:

Helps an agent access and manage OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using OurFamilyWizard can ask an agent to review co-parenting messages and schedules, manage shared expenses, and work with journal entries after connecting their account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to sensitive co-parenting records could expose private messages, contact details, expenses, and journal entries.

Mitigation: Connect only intentionally, use the narrowest available deployment mode, and avoid sharing retrieved records beyond the intended audience.

Risk: Plaintext credential setup could leave account credentials in project files or version control.

Mitigation: Keep credentials out of project files and version control, and restrict configuration file permissions.

Risk: Reading messages or making changes can alter a sensitive co-parenting record, sometimes irreversibly.

Mitigation: Warn before marking messages read, and require explicit user confirmation before sends, deletions, expenses, events, attachments, or journal actions.

## Reference(s):

- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and structured account summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize sensitive account records; live status and completeness should be checked before making current-state claims.]

## Skill Version(s):

2.20.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
