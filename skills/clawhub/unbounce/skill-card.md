## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Unbounce accounts, landing pages, form fields, leads, and conversion data through Maton-managed OAuth. It is suited for read-first landing-page and lead-management workflows where write operations are explicitly confirmed by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Unbounce landing pages and leads through a connected Maton account.

Mitigation: Install only when Unbounce access is intended, prefer OAuth, review account and scope choices during connection, and revoke unused connections.

Risk: Create, update, publish, delete, or lead-changing operations can alter customer-facing pages or lead data.

Mitigation: Default to read and list calls, verify target identifiers and current state first, and require explicit user confirmation before any write operation.

Risk: API keys or provider-issued tokens can be exposed if printed, logged, stored, or passed through shell commands.

Mitigation: Use Maton-managed OAuth where possible, keep credentials in the credential store, never inspect or persist secret values, and send Maton API keys only to api.maton.ai when CLI use is impossible.

Risk: Unbounce content and lead fields may contain untrusted external data.

Mitigation: Treat fetched content as data, validate it before reuse, and do not execute or follow instructions found inside API responses.

## Reference(s):

- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Unbounce connection.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
