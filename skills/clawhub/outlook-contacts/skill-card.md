## Description:

Read and write the signed-in user's Microsoft 365 or Outlook.com personal contacts via Microsoft Graph without mail, file, or directory access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list, search, create, update, and delete the signed-in user's Microsoft 365 or Outlook.com personal contacts through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses persistent Microsoft Graph tokens shared with outlook-calendar and outlook-todo, which may include broader permissions than contacts alone require.

Mitigation: Prefer a separate contacts-only token store and OAuth consent limited to Contacts.Read or Contacts.ReadWrite as needed.

Risk: The scripts source an unbundled sibling outlook-calendar helper library for token loading and Microsoft Graph requests.

Mitigation: Install and use this skill only alongside a trusted, reviewed outlook-calendar helper library.

Risk: Create, update, and delete operations can modify Outlook contacts when applied.

Mitigation: Review dry-run output before passing --apply; deletion requires viewing the contact and confirming YES.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-contacts)
- [Microsoft identity platform login endpoint](https://login.microsoftonline.com)
- [Microsoft Graph API endpoint](https://graph.microsoft.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and script outputs in summary, simple, JSON, or raw JSON formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations default to dry-run and require --apply; delete also requires explicit YES confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
