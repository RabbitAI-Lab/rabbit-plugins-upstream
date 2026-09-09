## Description:

Systeme.io API integration with managed OAuth for managing contacts, tags, courses, communities, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Systeme.io account data through Maton, including contacts, tags, course enrollments, community memberships, and subscriptions. It is suited for read-first API workflows where write operations are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Systeme.io access through Maton and requires trust in that gateway for the connected account.

Mitigation: Install it only when Maton is an acceptable gateway, review requested connection scopes, and connect only the account needed for the task.

Risk: Write operations can change contacts, enrollments, memberships, subscriptions, or other account data.

Mitigation: Default to read and list calls first, then require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Long-lived API keys or provider tokens can be exposed through logs, command lines, files, or copied output.

Mitigation: Prefer OAuth via the Maton CLI credential store, never print or persist credentials, and use environment-held API keys only when the CLI cannot be installed.

Risk: Data returned by Systeme.io may contain untrusted or adversarial content.

Mitigation: Treat API responses as data, validate values before reuse, and never execute or follow instructions contained in fetched records.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Systeme.io API Reference](https://developer.systeme.io/reference)
- [Systeme.io API Overview](https://developer.systeme.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Systeme.io connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
