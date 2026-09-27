## Description:

Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to connect a Google Forms account through Maton, read form metadata and responses, create forms and questions, and run approved automations against that connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Forms account access or form data may be exposed if broad OAuth scopes, long-lived API keys, or full raw responses are used unnecessarily.

Mitigation: Prefer OAuth, approve only the scopes and account needed for the task, avoid exported API keys, and return only the response fields the user needs.

Risk: Write operations, new connections, hosted functions, triggers, or deletions can modify user data or automate future actions.

Mitigation: Require explicit user approval for each write, connection, function, trigger, invocation, and deletion; remove unused connections, functions, triggers, and destinations when finished.

Risk: Third-party trigger destinations or hosted functions with network access can send connected account data to unintended hosts.

Mitigation: Use only destinations the user named and trusts, review hosts individually, and prefer hosted functions deployed with outbound network access denied.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-forms)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Forms API Overview](https://developers.google.com/workspace/forms/api/reference/rest)
- [Google Forms Get Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/get)
- [Google Forms Create Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create)
- [Google Forms Batch Update](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate)
- [Google Forms List Responses](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated Google Forms API requests, Maton CLI commands, hosted function examples, and trigger configuration.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
