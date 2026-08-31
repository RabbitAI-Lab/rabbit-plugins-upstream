## Description:

Cognito Forms API integration with managed OAuth for accessing forms, entries, and documents through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to list Cognito Forms resources, create or modify entries with approval, and retrieve documents or files through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Cognito Forms account data through a Maton-mediated connection.

Mitigation: Prefer OAuth, choose the narrowest available Cognito Forms scopes, and confirm the intended account or connection before use.

Risk: Write or delete API calls can modify or remove Cognito Forms entries.

Mitigation: Default to read and list calls, then require explicit user approval with the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or command-line arguments when the CLI is unavailable.

Mitigation: Use the Maton CLI with OAuth when possible; if raw HTTP is required, never print or persist the key and feed authorization headers through stdin.

Risk: Content returned by Cognito Forms may include untrusted instructions or data.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions contained in fetched form content.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Cognito Forms API Overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Cognito Forms REST API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/rest-api-reference)
- [Cognito Forms API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/api-reference)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance, Code]

**Output Format:** [Markdown guidance with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Cognito Forms account.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
