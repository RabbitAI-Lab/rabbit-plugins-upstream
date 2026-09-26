## Description:

Zoho CRM API integration with managed OAuth for reading, creating, updating, deleting, searching, and managing CRM records, organization settings, users, and module metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, developers, and agents use this skill to manage Zoho CRM data through an authorized Maton connection. It supports CRM record operations, searches, module metadata lookups, and approved automation patterns for functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Zoho CRM business data through an authorized Maton connection.

Mitigation: Use OAuth where possible, default to read-only/list operations, and require explicit approval before writes, new connections, function deployment, trigger setup, or other automation.

Risk: Persistent triggers or destinations can keep forwarding matching events after setup.

Mitigation: Keep destinations on trusted Maton URLs unless the user intentionally approves another host, disclose what data will flow and how often, and remove unused triggers, destinations, functions, and connections when finished.

Risk: API keys and broad OAuth scopes can increase the impact of misuse or accidental exposure.

Mitigation: Prefer OAuth, choose least-privilege scopes when available, avoid exporting long-lived credentials to child processes, and revoke unused authorizations.

## Reference(s):

- [ClawHub Zoho CRM Skill](https://clawhub.ai/byungkyu/skills/zoho-crm)
- [Maton Homepage](https://maton.ai)
- [Zoho CRM API v8 Documentation](https://www.zoho.com/crm/developer/docs/api/v8/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CRM API request guidance, Maton CLI commands, hosted function examples, trigger configuration guidance, and safety checks for writes or automation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
