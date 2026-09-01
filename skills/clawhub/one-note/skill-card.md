## Description:

OneNote API integration with managed OAuth via Microsoft Graph for accessing and managing notebooks, sections, section groups, and pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, organize, create, and update Microsoft OneNote notebooks and pages through Maton-managed Microsoft Graph access. It is suited for note organization workflows where the user can approve account connections and any write or delete action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify OneNote content through a connected Microsoft account.

Mitigation: Use OAuth where possible, approve new connections intentionally, and confirm the target notebook, page, and payload before any write or delete action.

Risk: API-key fallback uses a long-lived credential when the Maton CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; use the API-key fallback only when necessary and avoid printing, logging, persisting, or passing the key on the command line.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [OneNote Page HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, API paths, JSON examples, HTML examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands and Microsoft Graph request payloads; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
