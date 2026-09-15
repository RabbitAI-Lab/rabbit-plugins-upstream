## Description:

Provides agent guidance for using ofw-mcp to work with OurFamilyWizard co-parenting messages, calendars, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to access and manage OurFamilyWizard co-parenting records through ofw-mcp, including messages, calendar events, shared expenses, and journal entries. The skill is intended to support careful review workflows around sensitive family and legal records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned third-party code that receives OFW credentials.

Mitigation: Pin and review the ofw-mcp package or source version before installation, and avoid passing OFW passwords directly in shell command history.

Risk: Configuration files may contain credentials for a sensitive co-parenting account.

Mitigation: Store credentials only in protected local configuration or environment files and restrict access to those files.

Risk: The skill can perform broad writes to messages, calendar entries, expenses, and journal records.

Mitigation: Require explicit user confirmation for every send, delete, expense, calendar, or journal write operation.

Risk: Some reads can change user-visible state, including marking messages read or updating last-seen status.

Mitigation: Warn the user before actions that can mark messages read or update seen status, and prefer read-only or draft/review workflows when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp GitHub project](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Tool call instructions]

**Output Format:** [Markdown with JSON snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes safety notes for credential handling, cache freshness, irreversible sends, mark-as-read behavior, and write confirmations.]

## Skill Version(s):

2.16.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
