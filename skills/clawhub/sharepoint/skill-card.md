## Description:

Microsoft SharePoint guides agents through SharePoint site, list, document library, and file operations via Microsoft Graph using Maton-managed OAuth or a Maton API key fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to inspect and manage SharePoint sites, lists, document libraries, files, sharing links, and versions through Maton-mediated Microsoft Graph calls. It is intended for SharePoint document management, list operations, site content workflows, and troubleshooting while defaulting to read/list operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SharePoint or Maton credentials could be exposed through logs, command lines, files, or raw HTTP fallback handling.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, avoid command-line secrets, and send Maton API keys only to api.maton.ai when the CLI cannot be installed.

Risk: Write, delete, upload, or sharing operations can modify content, revoke access, or expose SharePoint data.

Mitigation: Default to read/list calls and require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, DELETE, upload, delete, or sharing-link operations.

Risk: Ambiguous Maton profiles or multiple SharePoint connections can route a request to the wrong account or tenant.

Mitigation: List active connections, match the intended connection ID, and specify the connection or profile when more than one candidate exists.

Risk: SharePoint responses may contain personal, confidential, or adversarial content.

Mitigation: Extract only fields needed for the task, avoid dumping raw responses into logs or files, and treat retrieved content as untrusted data rather than executable instructions.

Risk: The Maton API passthrough can reach endpoints beyond the examples documented by the skill if the connected account permits them.

Mitigation: Use least-privilege SharePoint scopes, prefer read-only access where possible, and apply the same confirmation rules to every passthrough endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Graph SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [Microsoft Graph DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Microsoft Graph List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should minimize returned SharePoint data and require explicit confirmation before connection creation, writes, uploads, deletes, sharing changes, or other high-impact operations.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
