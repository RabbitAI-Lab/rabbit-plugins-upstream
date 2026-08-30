## Description:

Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Google Contacts through Maton OAuth, including listing, creating, updating, deleting, and searching contacts and contact groups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Google Contacts data through Maton-mediated access.

Mitigation: Prefer OAuth, choose the narrowest available account and scopes, default to read and list calls, and confirm all write or delete operations with the user.

Risk: Deleting a contact group with deleteContacts=true can delete the contacts in the group.

Mitigation: Confirm the specific group, intended effect, and deleteContacts value before running the delete operation.

Risk: Long-lived Maton API keys can be exposed through command lines, logs, shell history, or child processes when OAuth is not used.

Mitigation: Use OAuth when possible; if raw HTTP is necessary, feed authorization headers through stdin, never print the key, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Contacts connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
