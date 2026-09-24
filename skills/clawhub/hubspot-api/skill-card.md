## Description:

HubSpot API integration with managed OAuth for CRM contacts, companies, deals, associations, and properties, with read-first guidance and user approval for writes or new connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with HubSpot CRM records through Maton-managed OAuth, including listing, searching, creating, and updating contacts, companies, deals, associations, and properties. Hosted functions and triggers support user-approved automation around HubSpot events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth access can reach whatever HubSpot scopes the user grants through Maton.

Mitigation: Use least-privilege HubSpot scopes and confirm the intended HubSpot account and connection before any write or new connection.

Risk: Hosted functions and triggers can automate HubSpot actions and may process CRM personal data.

Mitigation: Review each function or trigger before use, prefer DENY_ALL network policy where applicable, and require explicit user approval for deployment, invocation, or write operations.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is necessary, avoid logging, printing, persisting, or passing the key on a command line.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton Homepage](https://maton.ai)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HubSpot CRM API paths, Maton CLI commands, OAuth connection guidance, and function or trigger configuration examples.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
