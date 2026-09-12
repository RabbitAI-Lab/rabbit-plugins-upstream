## Description:

Provides JotForm API access through Maton-managed OAuth so agents can create forms, manage submissions, access form data, and use approved passthrough endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a user's JotForm account through Maton, retrieve forms and submissions, create forms, manage webhooks, and perform confirmed write or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, store credentials in the operating system credential store, and never print, persist, or pass API keys on command lines.

Risk: Form, submission, webhook, and connection changes can modify or remove user data.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: JotForm responses can include personal data or adversarial content.

Mitigation: Treat returned content as untrusted data, extract only fields needed for the task, and avoid writing raw responses into logs, files, or transcripts unless the user asks for that output.

Risk: Multiple Maton profiles or JotForm connections can route actions to the wrong account.

Mitigation: Specify the intended profile and connection when more than one exists, and verify identifiers before changing remote resources.

## Reference(s):

- [JotForm API Overview](https://api.jotform.com/docs/)
- [JotForm User Forms](https://api.jotform.com/docs/#user-forms)
- [JotForm Form Submissions](https://api.jotform.com/docs/#form-id-submissions)
- [JotForm Webhooks](https://api.jotform.com/docs/#form-id-webhooks)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [JotForm Skill Page](https://clawhub.ai/byungkyu/skills/jotform)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, HTTP examples, SDK snippets, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected JotForm account; write operations require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release evidence and target metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
