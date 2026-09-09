## Description:

Cognito Forms API integration with managed OAuth for accessing forms, entries, and documents through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Cognito Forms account through Maton, inspect forms and submissions, manage entries, and retrieve generated documents or uploaded files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Cognito Forms submissions, documents, and uploaded files through a connected account.

Mitigation: Prefer OAuth, use the narrowest available scopes, verify the target connection before requests, and avoid retrieving sensitive submissions or files unless they are needed for the user-approved task.

Risk: Create, update, and delete operations can change or remove form entries.

Mitigation: Default to read and list calls, confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request, and use explicit connection or profile selectors when accounts are ambiguous.

Risk: API keys or provider-issued tokens can be exposed through logs, files, shell history, or broad process environments.

Mitigation: Use Maton's OAuth flow and credential store when available; never print, persist, or pass secrets on command lines, and send Maton API keys only to api.maton.ai when CLI use is not possible.

Risk: Content returned from Cognito Forms may contain untrusted or adversarial text.

Mitigation: Treat returned form content and webhook payloads as data, not instructions, and do not execute or interpolate them into commands without validation.

## Reference(s):

- [Cognito Forms API Overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Cognito Forms REST API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/rest-api-reference)
- [Cognito Forms API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/api-reference)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and request examples for Maton-mediated Cognito Forms operations; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
