## Description:

Lemlist API integration with managed OAuth for managing sales automation and cold outreach workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a Lemlist account through Maton and manage campaigns, leads, activities, schedules, sequences, and unsubscribes. It is intended for read-first account operations with explicit confirmation before new connections or write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a real Lemlist sales-outreach account, including campaign, lead, schedule, unsubscribe, and other write operations.

Mitigation: Use OAuth where possible, verify the exact connection and account, and require explicit user review before any write operation.

Risk: Creating or changing campaigns, leads, sequences, schedules, unsubscribes, or outreach activity can affect recipients and account reputation.

Mitigation: Default to read and list calls first, then confirm target resources, payloads, and intended effects before POST, PUT, PATCH, or DELETE calls.

Risk: Fallback API-key use can expose a long-lived Maton credential if printed, persisted, passed on a command line, or sent to the wrong host.

Mitigation: Prefer OAuth; when fallback HTTP access is necessary, keep the key out of logs and command arguments, avoid persistence, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/lemlist)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Lemlist API documentation](https://developer.lemlist.com/)
- [Lemlist API reference](https://developer.lemlist.com/api-reference)
- [Lemlist Help Center - API](https://help.lemlist.com/en/collections/17109856-api-webhooks)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Lemlist API operations; generated commands may read or modify the connected Lemlist account.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
