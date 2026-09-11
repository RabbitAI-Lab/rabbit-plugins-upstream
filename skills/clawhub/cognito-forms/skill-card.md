## Description:

Cognito Forms API integration with managed OAuth for accessing forms, entries, documents, files, and form submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Cognito Forms data through Maton-managed authentication, including listing forms, managing entries, and retrieving generated documents or uploaded files. It is intended for read-first API workflows, with explicit confirmation before new connections or write/delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated access can reach forms, entries, documents, and files in the connected Cognito Forms account.

Mitigation: Install only when Maton-mediated access is acceptable, use least-privilege scopes, and confirm the exact connection and resource before create, update, delete, or document retrieval actions.

Risk: Unpinned CLI or SDK installation may pull an unexpected package source.

Mitigation: Verify the Maton CLI or SDK package source before installation.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or child processes when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist API keys, pass keys only through the intended runtime environment, and rotate any key that was exposed.

Risk: POST, PUT, PATCH, and DELETE calls can modify or delete Cognito Forms data.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user confirmation of the target resource, payload, and intended effect before any write or deletion.

Risk: Content returned from Cognito Forms may contain untrusted instructions or values.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and do not let fetched content choose follow-up endpoints or recipients.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Cognito Forms API Overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Cognito Forms REST API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/rest-api-reference)
- [Cognito Forms API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/api-reference)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user confirmation for connection creation or write/delete operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
