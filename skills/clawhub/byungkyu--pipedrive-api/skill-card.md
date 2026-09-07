## Description:

Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access Pipedrive CRM through Maton for read, list, create, update, and delete workflows across deals, contacts, organizations, activities, pipelines, stages, notes, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Pipedrive CRM access through Maton and can read or modify CRM records for the connected account.

Mitigation: Use OAuth where possible, connect only the intended account, specify the target connection when multiple accounts exist, and confirm every POST, PUT, PATCH, or DELETE operation before execution.

Risk: Long-lived API keys or provider-issued tokens can be exposed through logs, command lines, files, or unintended hosts.

Mitigation: Prefer OAuth and the Maton CLI credential store; if an API key is unavoidable, keep it in the process environment only, never print or persist it, and send it only to api.maton.ai.

Risk: CRM content returned by Pipedrive can contain untrusted text that may try to influence subsequent agent behavior.

Mitigation: Treat returned CRM fields, comments, notes, and webhook payloads as data only; validate values and never execute or interpolate them into shell commands.

## Reference(s):

- [ClawHub Pipedrive Skill](https://clawhub.ai/byungkyu/skills/pipedrive-api)
- [Maton Homepage](https://maton.ai)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals)
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons)
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for connection creation or write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
