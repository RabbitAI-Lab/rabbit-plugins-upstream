## Description:

Granola MCP integration with managed authentication for searching meeting content, retrieving summaries and action items, and accessing transcripts from Granola via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a user's Granola account through Maton, then answer questions about meetings, retrieve meeting lists or details, and access transcripts when the user has authorized that access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Granola meeting notes, transcripts, summaries, attendee details, and related business context through the connected account.

Mitigation: Prefer OAuth, connect only the account needed for the task, request the narrowest meeting data needed, return only relevant excerpts, and avoid storing or logging raw meeting content.

Risk: Long-lived Maton API keys or broad automation settings can expose account access beyond the immediate task.

Mitigation: Use OAuth when possible, avoid environment API keys unless the CLI cannot be installed, approve each connection or automation explicitly, keep triggers and destinations narrowly scoped, and remove unused connections, functions, or destinations.

## Reference(s):

- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Granola Skill on ClawHub](https://clawhub.ai/byungkyu/skills/granola-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Code]

**Output Format:** [Markdown with inline bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands or request payloads that access sensitive meeting notes, summaries, attendees, and transcripts through the user's authorized Granola connection.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
