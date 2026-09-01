## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Unbounce accounts, pages, leads, domains, and users through managed Maton authentication. It supports read-first API workflows and requires explicit user approval before creating connections or modifying Unbounce data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Unbounce through Maton grants access to landing page and lead data in the connected account.

Mitigation: Prefer OAuth with the Maton CLI, connect only the needed Unbounce account, and approve each new connection explicitly.

Risk: Write operations can modify or delete Unbounce resources or create lead data.

Mitigation: Default to read and list calls, verify target identifiers first, and confirm the payload and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Long-lived API keys can be exposed if they are printed, persisted, or passed on a command line.

Mitigation: Avoid MATON_API_KEY unless the CLI cannot be used; when needed, keep it out of shell history, files, and logs.

Risk: Unbounce API responses, including lead fields, may contain untrusted content.

Mitigation: Treat fetched content as data, validate it before reuse, and do not execute or interpolate it into shell commands.

## Reference(s):

- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/unbounce)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-oriented command guidance and API response examples; write and connection operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
