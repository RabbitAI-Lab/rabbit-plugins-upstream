## Description:

Microsoft SharePoint provides SharePoint API integration via Microsoft Graph with managed OAuth for sites, lists, document libraries, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and perform SharePoint document, list, library, site, sharing, version, and search operations through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or change SharePoint data using user-authorized credentials.

Mitigation: Prefer read and list calls first, require explicit user confirmation before write, delete, or share actions, and verify the target resource and payload before execution.

Risk: Multiple Maton accounts or SharePoint connections can cause requests to target the wrong tenant or site.

Mitigation: Specify the intended profile and connection when more than one account or connection exists.

Risk: API keys and provider-issued tokens can leak through environment variables, logs, command lines, or copied output.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, avoid printing or persisting tokens, and send Maton API keys only to api.maton.ai.

Risk: Documented install commands do not pin reviewed Maton package versions.

Mitigation: Pin or isolate Maton CLI and SDK package versions when deploying in controlled environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Maton Homepage](https://maton.ai)
- [SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SharePoint and Microsoft Graph identifiers, request bodies, and response-field guidance.]

## Skill Version(s):

1.2.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
