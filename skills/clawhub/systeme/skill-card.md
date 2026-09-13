## Description:

Systeme.io API integration with managed OAuth for managing contacts, contact tags, contact custom fields, tags, course enrolments, community memberships, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Systeme.io accounts through Maton-managed authentication, with read/list workflows first and explicit confirmation for account connections, writes, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection-level permissions can expose or modify Systeme.io business data.

Mitigation: Use OAuth with the narrowest available scopes, specify the intended connection for writes, and require explicit user review before mutations.

Risk: The raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Prefer the Maton CLI OAuth flow; when raw HTTP is unavoidable, do not print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Hosted functions, triggers, and webhooks can create ongoing automation beyond a one-time API call.

Mitigation: Use these only when the user explicitly asks for persistent automation, review the handler and destination before approval, and prefer a deny-all network policy for hosted functions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/systeme)
- [Maton Homepage](https://maton.ai)
- [Systeme.io API Reference](https://developer.systeme.io/reference)
- [Systeme.io API Overview](https://developer.systeme.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
