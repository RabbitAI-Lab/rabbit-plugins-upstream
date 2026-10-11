## Description:

Connects an agent to Google Contacts and the People API for contact management, Workspace directory searches, and profile lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams using an agent with an authorized Google account can search and manage personal contacts, look up Workspace directory profiles, and inspect reporting relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion and merging paths do not consistently enforce confirmation.

Mitigation: Enable GOG_READONLY=1 unless writes are needed; require human review before deletion, dedupe apply, or gog_contacts_run.

Risk: An authorized Google account and its persistent credentials can be exposed on a shared or weakly isolated host.

Mitigation: Use an isolated host and protect the persistent keyring and data directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli CLI dependency](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text or JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain personal contact and Workspace directory information.]

## Skill Version(s):

4.7.1 (source: ClawHub release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
