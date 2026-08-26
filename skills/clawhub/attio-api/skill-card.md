## Description:

Attio API integration with managed OAuth for managing CRM data including people, companies, custom objects, tasks, notes, comments, lists, meetings, and workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Attio CRM data through Maton OAuth, inspect CRM objects and records, and perform approved create, update, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or modify CRM data in the authorized Attio account.

Mitigation: Use OAuth where possible, select the narrowest available scopes, confirm the target connection, and review create, update, or delete payloads before execution.

Risk: A long-lived Maton API key can leak through shell history, process listings, logs, or persisted files when the CLI cannot be used.

Mitigation: Prefer Maton OAuth; if raw HTTP is required, pass credentials through stdin or a secret manager, never print or persist the key, and rotate it if exposed.

Risk: Writes, deletions, messaging, scheduling, sharing, or automation operations can have high-impact side effects.

Mitigation: Default to read and list operations first, then require explicit user approval with resource identifiers, payload, and intended effect before POST, PUT, PATCH, or DELETE calls.

Risk: CRM content returned by Attio may contain untrusted instructions or adversarial text.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into shell commands, and keep endpoint and recipient choices under user control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/attio-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Attio API Overview](https://docs.attio.com/rest-api/overview)
- [Attio API Reference](https://docs.attio.com/rest-api/endpoint-reference)
- [Attio Records API](https://docs.attio.com/rest-api/endpoint-reference/records)
- [Attio Objects API](https://docs.attio.com/rest-api/endpoint-reference/objects)
- [Attio Tasks API](https://docs.attio.com/rest-api/endpoint-reference/tasks)
- [Attio Rate Limiting](https://docs.attio.com/rest-api/guides/rate-limiting)
- [Attio Pagination](https://docs.attio.com/rest-api/guides/pagination)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Attio API requests; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
