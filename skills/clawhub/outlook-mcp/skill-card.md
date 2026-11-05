## Description:

Connects agents to personal Outlook mail, inbox rules, calendars, contacts, tasks, drafts, and attachments through Microsoft Graph, with configurable permissions and no telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Individuals and developers using AI agents with personal Outlook accounts use this server to read and manage mail, calendars, contacts, and tasks through Microsoft Graph. Drafting and other write actions are available according to the account and the user's configured permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mail, calendar, contact, and task tools can expose sensitive account data; enabled write tools can change data or send messages.

Mitigation: Start with read_only enabled and allow only needed write categories. For Microsoft-enforced read-only access, use a separate read-only app registration with read_only_consent enabled. Review calendar changes that may notify participants.

Risk: Remote HTTP access sends requests and responses over the network, and the server does not provide TLS.

Mitigation: Use a TLS-terminating proxy for remote access and protect the endpoint with its required bearer token.

Risk: Optional document parsing is disclosed as lacking sandboxing.

Mitigation: Keep document parsing disabled unless its lack of sandboxing is acceptable.

Risk: On Linux without an available keyring, the token cache may use a plaintext file if that option is enabled.

Mitigation: Use an OS-backed keyring where available; enable unencrypted token storage only when its storage risks are acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Project repository](https://github.com/mpalermiti/outlook-mcp)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)

## Skill Output:

**Output Type(s):** [Structured data, Text, Files]

**Output Format:** [Structured JSON and text responses; attachment content when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the Outlook account, enabled tools, and requested fields. Attachment access follows configured paths and size limits.]

## Skill Version(s):

1.31.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
