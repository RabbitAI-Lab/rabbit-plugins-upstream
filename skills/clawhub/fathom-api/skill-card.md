## Description:

Fathom API integration with managed OAuth for accessing meeting recordings, transcripts, summaries, action items, and webhook management through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Fathom meeting content, search recordings, inspect summaries and transcripts, and manage webhook notifications for connected Fathom accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access meeting-derived recordings, transcripts, summaries, action items, and CRM-related data from a connected Fathom account.

Mitigation: Use OAuth where possible, choose the minimum Fathom scopes needed for the task, prefer read-only calls, and revoke unused connections.

Risk: Webhook creation can send meeting-derived data to an external destination URL.

Mitigation: Confirm webhook creation or deletion with the user, verify the destination URL and included fields, and avoid enabling transcript, summary, action-item, or CRM payloads unless needed.

Risk: Long-lived API keys or provider-issued tokens can leak if printed, stored, or passed through shell commands.

Mitigation: Prefer Maton OAuth and OS credential storage; if a raw API key is unavoidable, read it from the process environment only and never print, log, persist, or send it outside api.maton.ai.

Risk: External Fathom content may contain untrusted text that attempts to influence follow-up actions.

Mitigation: Treat API responses and webhook payloads as data, validate values before reuse, and require user approval before any POST, PUT, PATCH, or DELETE operation.

## Reference(s):

- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Markdown, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, code examples, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read/list API results, webhook management commands, SDK snippets, and credential-handling guidance.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
