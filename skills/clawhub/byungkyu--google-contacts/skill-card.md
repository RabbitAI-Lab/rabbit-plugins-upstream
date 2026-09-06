## Description:

Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book search through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a user's Google Contacts account through Maton, then list, search, create, update, delete, and organize contacts and contact groups with user-directed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker access to a user's Google Contacts account and contact data through Maton.

Mitigation: Install only when that access is intended, prefer OAuth, use least-privilege scopes when offered, and extract only the contact fields needed for the task.

Risk: Create, update, batch, and delete operations can modify or remove contacts or contact groups.

Mitigation: Default to read and list calls first, then confirm the exact resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Multiple Maton profiles or Google Contacts connections can route a request to the wrong account.

Mitigation: Specify the intended profile and connection when more than one account or connection exists, especially before writes or deletions.

Risk: Raw HTTP fallback with MATON_API_KEY uses a long-lived credential that can leak through logs, shell history, files, or child processes.

Mitigation: Use raw HTTP only where the CLI cannot be installed, never print or persist the key, pass it through the environment only, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with CLI commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read/list defaults, OAuth, explicit approval for writes and connection changes, and data minimization for contact responses.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
