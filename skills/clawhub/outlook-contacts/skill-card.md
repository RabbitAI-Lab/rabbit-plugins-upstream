## Description:

Read and write the signed-in user's Microsoft 365 or Outlook.com personal contacts through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to list, search, create, update, or delete personal Outlook contacts when answering contact lookup or contact maintenance requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Microsoft Graph token may include contacts, calendar, and task permissions beyond the immediate contacts workflow.

Mitigation: Use this skill only when that shared consent is acceptable; prefer a contacts-only token/cache if available and keep ~/.outlook-graph owner-only.

Risk: The contacts scripts execute a helper from the outlook-calendar skill package.

Mitigation: Verify the referenced outlook-calendar helper before using the contacts skill, especially before write operations.

Risk: Create, update, and delete operations can modify personal Outlook contacts.

Mitigation: Review dry-run payloads, use --apply only after checking the proposed change, and rely on the delete confirmation prompt before removal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-contacts)
- [Microsoft Graph API](https://graph.microsoft.com)
- [Microsoft identity platform login](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and text, summary, JSON, or raw JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands can return paginated contact summaries or JSON; write commands default to dry-run and require --apply for changes.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
