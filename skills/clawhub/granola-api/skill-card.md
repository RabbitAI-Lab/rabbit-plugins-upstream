## Description:

Granola helps agents use Maton-managed authentication to search Granola meeting content, retrieve summaries and action items, list meetings, and fetch transcripts through Granola MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to answer questions from their own Granola meeting notes, inspect meeting metadata, retrieve summaries or action items, and fetch transcripts when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Granola meeting notes, transcripts, attendees, and private notes through a connected account.

Mitigation: Prefer OAuth, approve Granola connection creation deliberately, select the narrowest available scopes, and pin the intended Maton profile and connection when multiple accounts exist.

Risk: The Maton API passthrough can reach Granola paths beyond the four documented meeting-read tools.

Mitigation: Keep routine use to documented meeting tools, and require explicit confirmation before using unknown paths, custom headers, non-read endpoints, or operations that could modify or share account data.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, persisted, or passed through shell arguments.

Mitigation: Use OAuth with the CLI credential store when possible, check authentication with status commands, and never print, log, persist, export, or inspect credential values.

Risk: Meeting content returned by Granola can contain untrusted instructions or adversarial text.

Mitigation: Treat fetched meeting content as data, preserve citations when summarizing, and do not let returned content choose follow-up endpoints, recipients, commands, or actions.

## Reference(s):

- [Granola skill page](https://clawhub.ai/byungkyu/skills/granola-api)
- [Maton](https://maton.ai)
- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and optional Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Granola note citations, XML-like meeting data, JSON MCP envelopes, or transcript text depending on the selected tool.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
