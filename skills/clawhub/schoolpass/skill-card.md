## Description:

This skill helps an agent answer questions about a child's SchoolPass arrival and dismissal details through a parent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or delegated agents use this skill to read SchoolPass parent-account information such as linked students, dismissal calendars, pickup changes, authorized drivers, dismissal locations, and school details. It can also propose and submit or cancel real dismissal changes only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive child and parent data through SchoolPass parent-account credentials.

Mitigation: Keep credentials out of source control and backups, avoid project-level credential files, restrict credential-file permissions, and never echo passwords or session tokens into conversations.

Risk: The skill can submit or cancel real child dismissal changes.

Mitigation: Require explicit user confirmation before any dismissal submission or cancellation, and show the preview before making a change.

Risk: The setup runs an external MCP package without pinning a reviewed version.

Mitigation: Use a pinned, reviewed server version when available and review the package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)
- [schoolpass-mcp GitHub link listed in skill](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with tool-call guidance and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools default to compact responses; write tools require explicit confirmation before submitting or canceling dismissal changes.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
