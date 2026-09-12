## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an Unbounce account through Maton, inspect landing pages, leads, accounts, domains, users, and conversion data, and perform approved API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs credentialed access to an Unbounce account through Maton.

Mitigation: Install it only when Maton access to the target Unbounce account is intended, prefer OAuth, and confirm each new connection with the user.

Risk: Write operations and connection deletion can modify or remove Unbounce data or authorizations.

Mitigation: Default to read and list calls, verify resource identifiers first, and require explicit user approval before POST, PUT, PATCH, DELETE, or connection deletion.

Risk: Unbounce lead and user responses can contain personal information.

Mitigation: Request only the fields needed for the task and avoid dumping full API responses into logs, files, or user-visible output.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only when the CLI cannot be installed, never print or persist MATON_API_KEY, and send it only to api.maton.ai.

Risk: The API passthrough can reach endpoints beyond those documented in the skill when the connection permits it.

Mitigation: Treat the documented endpoints as the intended operating surface, use least privilege, and specify the target connection when more than one Unbounce connection exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/unbounce)
- [Maton Homepage](https://maton.ai)
- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Code, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include credentialed Unbounce API responses; lead data should be minimized because it can contain personal information.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
