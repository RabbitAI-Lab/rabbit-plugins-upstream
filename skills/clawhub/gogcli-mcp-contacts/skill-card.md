## Description:

Helps agents search and manage Google Contacts and query Google Workspace profiles and directory relationships through the People API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Users and developers use this skill to find personal contacts, search Workspace users, inspect profiles and reporting relationships, and manage contacts through an authenticated Google account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion or merging may be irreversible or affect the wrong person.

Mitigation: Do not authorize delete or dedupe apply until the exact target is independently confirmed and a backup or recovery plan exists.

Risk: Persistent Google credentials and broad account access expose personal contact and directory data.

Mitigation: Use GOG_READONLY=1 for lookup-only use, restrict Google account and OAuth scopes, and keep GOG_FILE_ROOTS narrow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or JSON contact and People API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain personal contact details and Workspace profile information.]

## Skill Version(s):

4.5.1 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
