## Description:

Attio API integration with managed OAuth for managing CRM data including people, companies, custom objects, tasks, notes, comments, lists, meetings, and related workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent read and manage Attio CRM resources through Maton-managed OAuth. It supports API lookups, record operations, task and note workflows, comments, lists, meetings, call recordings, pagination, troubleshooting, and SDK-oriented examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access CRM records and related workspace data in the connected Attio account.

Mitigation: Install it only when Attio CRM access through Maton is intended, use the narrowest available Attio scopes, and specify the intended connection when more than one account exists.

Risk: Create, update, delete, comment, note, task, and other write operations can change business records.

Mitigation: Require explicit user confirmation before every write operation, including the target resource, payload, and intended effect.

Risk: Long-lived API keys or provider tokens can leak if printed, logged, stored, or passed on a command line.

Mitigation: Prefer Maton OAuth and the CLI credential store; never expose credential values, and use raw API-key flows only when the CLI cannot be installed.

Risk: Multiple Maton profiles or Attio connections can route requests to the wrong workspace.

Mitigation: Use the appropriate profile and pass an explicit connection identifier whenever more than one relevant account or connection is available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/attio-api)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Attio connection; API calls may return JSON from Attio through Maton.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
