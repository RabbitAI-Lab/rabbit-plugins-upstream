## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access CallRail account, company, call, tracker, tag, user, integration, and notification data through Maton-managed authentication. It supports read-first analysis and selected account management tasks when the user confirms the target resource, payload, and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CallRail account access is mediated by Maton and may expose sensitive account, call, company, tracker, tag, user, integration, or notification data.

Mitigation: Confirm trust in Maton before installation, prefer OAuth over long-lived API keys, and authorize only the scopes and accounts needed for the current task.

Risk: POST, PUT, PATCH, or DELETE requests can modify or delete CallRail resources.

Mitigation: Default to read and list operations first, then require explicit user confirmation of the target resource, payload, and intended effect before any write operation.

Risk: Raw API responses can contain personal data such as names, email addresses, phone numbers, recordings, messages, or notes.

Mitigation: Extract only fields needed for the task and avoid logging, persisting, or broadly displaying full response payloads unless the user explicitly asks for them.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only when the CLI cannot be installed, never print or persist the key, pass it only through the process environment, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [CallRail Skill on ClawHub](https://clawhub.ai/byungkyu/skills/callrail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API call plans and commands; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
