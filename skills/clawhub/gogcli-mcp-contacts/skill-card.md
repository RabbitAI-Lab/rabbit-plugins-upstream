## Description:

Use this skill to search and manage Google Contacts and the broader Google People API, including contact lookups, Workspace directory searches, profile fields, and manager or report relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Employees and developers use this skill to search and manage personal Google Contacts and look up Google Workspace directory profiles, profile fields, and manager or report relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth setup may request permissions beyond those needed for Contacts and People API use.

Mitigation: Use a dedicated account with only necessary Contacts and People permissions, and reject unrelated OAuth requests.

Risk: Some contact deletion and merging operations lack a built-in approval check.

Mitigation: Keep GOG_READONLY=1 enabled for lookups. Before permitting writes, require host approval, back up contacts, and review an explicitly scoped merge preview.

## Reference(s):

- [Project repository (listed in artifact metadata)](https://github.com/chrischall/gogcli-mcp)
- [gogcli dependency](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured tool results and concise text responses; raw People API JSON is available for the raw lookup tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include contact details, directory profile fields, or raw People API JSON.]

## Skill Version(s):

4.9.1 (source: server-resolved release metadata, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
