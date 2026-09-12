## Description:

OneNote API integration with managed OAuth via Microsoft Graph for accessing and managing notebooks, sections, section groups, and pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent read, organize, create, and update OneNote content through Microsoft Graph via Maton. It is suited for notebook, section, section group, and page workflows where OAuth-managed access and explicit confirmation for changes are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic Microsoft Graph passthrough can reach endpoints beyond the documented OneNote workflows if the connection is authorized for them.

Mitigation: Use the smallest available OAuth scopes, prefer read-only access, specify the intended connection, and keep calls within the documented OneNote task scope.

Risk: Write, delete, and connection-management operations can change or revoke OneNote access and content.

Mitigation: Default to read and list calls, verify resource identifiers first, and require explicit user confirmation before POST, PUT, PATCH, DELETE, connection creation, or connection deletion.

Risk: Using a Maton API key or printing full API responses can expose credentials or personal notebook data.

Mitigation: Prefer OAuth through the CLI, never print or persist credentials, and return only the fields needed for the user's task.

## Reference(s):

- [Microsoft OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [Microsoft OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [Microsoft Graph OneNote HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Maton Homepage](https://maton.ai)
- [Maton Documentation](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/one-note)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with command examples, JSON examples, HTML snippets, and Python or JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Microsoft Graph paths, Maton CLI commands, OAuth connection handling guidance, and examples for minimizing returned OneNote data.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
