## Description:

OneNote API integration with managed OAuth via Microsoft Graph for accessing notebooks, sections, section groups, and pages through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, create, and manage OneNote notebooks, sections, section groups, and page content through Microsoft Graph. It is suited for note organization workflows where account connection and write operations require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton acts as the gateway for OneNote account access.

Mitigation: Install only if the user trusts Maton, prefer OAuth authentication, and have the user approve connection creation.

Risk: Create, update, copy, and delete operations can change OneNote data or connection state.

Mitigation: Default to read/list calls, verify resource identifiers first, and confirm the target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Deleting a connection is irreversible and can break automation that depends on that connection.

Mitigation: List connections, match the exact connection ID with the user, and avoid bypassing prompts unless the user has already confirmed the specific deletion.

Risk: Raw API-key use increases credential exposure risk.

Mitigation: Use the CLI with OAuth where possible, avoid exporting long-lived API keys, and reserve raw HTTP calls for environments where the CLI cannot be installed.

Risk: OneNote responses may contain personal or sensitive note content.

Mitigation: Extract only fields needed for the task and avoid logging, printing, or saving raw response payloads unless the user explicitly requests it.

## Reference(s):

- [Microsoft OneNote Skill on ClawHub](https://clawhub.ai/byungkyu/skills/one-note)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [OneNote Page HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Microsoft Graph calls through Maton and emphasize read/list defaults plus explicit user confirmation for writes.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
