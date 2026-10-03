## Description:

Helps agents search and manage Google Contacts and look up Workspace directory profiles and relationships through the People API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent connected to Google Contacts can find personal contacts and Workspace directory profiles, inspect relationships, and manage contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion or deduplication can permanently remove or merge records without sufficient enforced confirmation.

Mitigation: Restrict delete and dedupe tools to callers requiring explicit approval; use read-only mode for lookup-only access.

Risk: Google credentials persist in gog's local keyring or data directory.

Mitigation: Limit OAuth scopes and account access, protect stored credentials, and keep permitted file directories narrow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text or JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include personal contact and Workspace directory data.]

## Skill Version(s):

4.6.1 (source: server release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
