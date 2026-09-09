## Description:

Granola MCP integration with managed authentication for searching meeting content, retrieving meeting summaries, finding action items, and accessing transcripts via Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search and retrieve their Granola meeting notes, summaries, action items, metadata, and transcripts through Maton-managed MCP authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent access private Granola meeting notes through Maton.

Mitigation: Install only when this access is intended, prefer OAuth over API keys, and authorize only the needed Granola account and scopes.

Risk: Connection changes or non-read API calls can affect account state.

Mitigation: Default to read and list operations, and review requests to create or delete connections or perform non-read API calls before approval.

Risk: Meeting notes, transcripts, attendee details, and returned content may contain sensitive personal or business information.

Mitigation: Request only the meeting data needed for the task and avoid logging, storing, or copying raw responses unless the user asks for that handling.

## Reference(s):

- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/granola-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Granola meeting-note citations, metadata, summaries, action items, or transcript excerpts returned by the connected account.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
