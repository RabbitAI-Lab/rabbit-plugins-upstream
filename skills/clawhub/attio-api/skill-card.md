## Description:

Attio API integration with managed OAuth for managing CRM data including people, companies, custom objects, tasks, notes, comments, lists, meetings, and workspace records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, query, create, update, and delete Attio CRM records through Maton-managed OAuth or an approved Maton API key path. It is intended for CRM workflows where account selection, write confirmation, and response data minimization matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete CRM records and related Attio resources.

Mitigation: Default to read and list operations, verify identifiers and account context first, and require explicit user approval for every POST, PUT, PATCH, or DELETE request.

Risk: The Maton API passthrough can reach endpoints beyond the documented examples when the connected account permits them.

Mitigation: Use the narrowest Attio scopes available, specify the intended connection when more than one exists, and apply the same write-confirmation rules to every passthrough call.

Risk: API keys, provider-issued tokens, and CRM response bodies may expose sensitive credentials or personal data.

Mitigation: Prefer OAuth, keep credentials in the approved credential store or secret environment only, never print or persist tokens, and extract only the response fields needed for the task.

Risk: Deleting a Maton connection is irreversible and may break automations that rely on that connection.

Mitigation: List connections, confirm the exact connection identifier with the user, and omit force-style confirmation flags unless the specific deletion has already been approved.

## Reference(s):

- [Attio API Overview](https://docs.attio.com/rest-api/overview)
- [Attio API Reference](https://docs.attio.com/rest-api/endpoint-reference)
- [Attio Records API](https://docs.attio.com/rest-api/endpoint-reference/records)
- [Attio Objects API](https://docs.attio.com/rest-api/endpoint-reference/objects)
- [Attio Tasks API](https://docs.attio.com/rest-api/endpoint-reference/tasks)
- [Attio Rate Limiting](https://docs.attio.com/rest-api/guides/rate-limiting)
- [Attio Pagination](https://docs.attio.com/rest-api/guides/pagination)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/attio-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing API usage guidance and command examples; API responses may contain CRM personal data and should be minimized.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
