## Description:

Connects an agent to Google Contacts and the People API to search contacts, inspect Workspace profiles and relations, and manage personal contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent with an authorized Google account can look up contacts, search the Workspace directory, inspect profiles and reporting relations, and create, update, delete, or export contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deletion and duplicate merging can permanently change contact data without an operation-specific confirmation gate.

Mitigation: Preview duplicate merges, scope changes narrowly, and obtain user confirmation before deletion or applying merges.

Risk: Contact exports and directory lookups can disclose personal information.

Mitigation: Limit searches and exports to authorized data and review recipients and export destinations before sharing.

Risk: Connecting a Google account stores credentials that may be exposed on shared hosts.

Mitigation: Use the narrowest OAuth scopes, enable GOG_READONLY=1 for lookup-only use, and protect the credential keyring.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli dependency](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [MCP tool results, including contact and profile data; vCard (.vcf) files for exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected Google account and granted access.]

## Skill Version(s):

4.5.2 (source: ClawHub release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
