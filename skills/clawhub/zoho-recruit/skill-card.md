## Description:

Zoho Recruit API integration with managed OAuth for managing candidates, job openings, interviews, and recruitment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting operations users use this skill to read, create, update, search, and delete Zoho Recruit records through Maton-managed authentication. It is intended for candidate, job opening, interview, application, and related recruiting workflow tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Recruit records can contain sensitive candidate and recruiting data.

Mitigation: Retrieve only records needed for the task, summarize instead of exposing full records when possible, and require explicit approval before moving data to another app or destination.

Risk: Write and deletion operations can change recruiting workflows or permanently remove records.

Mitigation: Default to read/list calls, verify identifiers and current state first, and confirm the exact resource, payload, and effect before any POST, PUT, PATCH, or DELETE call.

Risk: Bulk delete requests can remove multiple opaque record IDs in one irreversible action.

Mitigation: Fetch and present each target record by module, name, and ID, then require item-level user approval for every ID before deletion.

Risk: API keys and provider-issued tokens can leak through logs, shell history, files, or command arguments.

Mitigation: Prefer OAuth and the Maton CLI credential store; never print, persist, inspect, or pass credentials on command lines, and send Maton API keys only to api.maton.ai.

Risk: The generic API passthrough can reach undocumented Zoho Recruit endpoints within the app path.

Mitigation: Use documented paths as written, avoid endpoint probing, and require explicit user approval with the exact method and endpoint for any undocumented call.

## Reference(s):

- [Zoho Recruit API v2 Overview](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Zoho Recruit Get Records API](https://www.zoho.com/recruit/developer-guide/apiv2/get-records.html)
- [Zoho Recruit Insert Records API](https://www.zoho.com/recruit/developer-guide/apiv2/insert-records.html)
- [Zoho Recruit Update Records API](https://www.zoho.com/recruit/developer-guide/apiv2/update-records.html)
- [Zoho Recruit Delete Records API](https://www.zoho.com/recruit/developer-guide/apiv2/delete-records.html)
- [Zoho Recruit Search Records API](https://www.zoho.com/recruit/developer-guide/apiv2/search-records.html)
- [Zoho Recruit Modules API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API request examples, JSON response examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read/list calls first, explicit approval for writes and deletions, least-privilege OAuth scopes, and careful handling of recruiting data.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
