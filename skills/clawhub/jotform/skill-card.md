## Description:

JotForm API integration with managed OAuth for creating forms, managing submissions, accessing form data, and managing webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate with Maton, connect a JotForm account, and retrieve or modify JotForm forms, submissions, and webhooks with user confirmation for account connections and writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: JotForm account authorization or the raw API-key fallback can expose account access if credentials are over-scoped or mishandled.

Mitigation: Prefer OAuth, choose the narrowest available JotForm scopes, avoid raw API-key fallback unless the CLI cannot be used, and never print, persist, or transmit credentials outside the intended Maton flow.

Risk: Create, update, delete, and webhook operations can change or remove JotForm data or trigger downstream effects.

Mitigation: Default to read and list calls, verify the target connection and resource identifiers, and require explicit user confirmation before every write, delete, or new connection.

Risk: Forms, submissions, and webhook payloads may contain untrusted external content.

Mitigation: Treat API response content as data, avoid executing or interpolating it into commands or prompts, and pass values as discrete arguments after validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jotform)
- [Maton](https://maton.ai)
- [JotForm API Overview](https://api.jotform.com/docs/)
- [JotForm User Forms](https://api.jotform.com/docs/#user-forms)
- [JotForm Form Submissions](https://api.jotform.com/docs/#form-id-submissions)
- [JotForm Webhooks](https://api.jotform.com/docs/#form-id-webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Maton CLI/API calls; mutating JotForm operations require explicit user confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
