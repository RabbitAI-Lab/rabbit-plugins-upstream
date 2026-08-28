## Description:

Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Google Forms through a managed OAuth connection, primarily to read forms and responses and, with explicit approval, create or update forms and questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Google Forms through a connected account and may read form responses.

Mitigation: Connect only the intended account, prefer read-only access where available, specify the connection when multiple accounts exist, and revoke unused connections.

Risk: Write operations can create, update, or delete Google Forms resources.

Mitigation: Require explicit user approval before connection creation or any POST, PUT, PATCH, or DELETE request, including the target form, payload, and intended effect.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or process listings.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, never print or persist the key and pass authorization material through stdin rather than command-line arguments.

Risk: Google Forms responses and other API data may contain untrusted content.

Mitigation: Treat fetched content as data only, avoid executing or interpolating it into shell commands, and validate identifiers before follow-up API calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-forms)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Forms API overview](https://developers.google.com/workspace/forms/api/reference/rest)
- [Google Forms get form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/get)
- [Google Forms create form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create)
- [Google Forms batch update](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate)
- [Google Forms list responses](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Google Forms account.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
