## Description:

Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Google Contacts through Maton-managed OAuth, including contact lookup, contact and group management, and address book search. It is intended for workflows that need controlled Google Contacts API calls with explicit approval before connection creation or data modification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Contacts access is routed through Maton, introducing dependence on a third-party gateway for contact data operations.

Mitigation: Install only if this routing is acceptable, verify the Maton CLI source before use, and prefer OAuth over long-lived API keys.

Risk: Creating, updating, or deleting contacts, contact groups, or connections can alter user address book data.

Mitigation: Default to read-only calls and require explicit user confirmation before any connection creation or POST, PUT, PATCH, or DELETE operation.

Risk: Multiple Maton profiles or Google Contacts connections can cause actions to apply to the wrong account.

Mitigation: Specify the intended Maton profile and connection when more than one is available, and verify identifiers before write operations.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, command lines, files, or copied output.

Mitigation: Prefer OAuth, never print or persist credentials, pass keys only through controlled process environments when the CLI is unavailable, and rotate any exposed key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, Google Contacts API paths, request payload examples, SDK snippets, and operational safety guidance.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
