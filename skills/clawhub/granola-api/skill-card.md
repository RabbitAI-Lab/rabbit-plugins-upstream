## Description:

Granola helps agents search, summarize, list, and retrieve transcripts from a user's Granola meeting notes through Maton-managed MCP access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Granola meeting notes, find summaries and action items, list meetings, and retrieve selected meeting details or transcripts through authenticated MCP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes, transcripts, private notes, participant identities, and provider responses may contain sensitive personal or business information.

Mitigation: Retrieve only the meetings and fields needed for the user's task, prefer query-based summaries when possible, and avoid copying raw responses to files, logs, or unrelated destinations.

Risk: OAuth tokens, Maton API keys, and provider-issued credentials can be exposed through command output, environment variables, logs, shell history, or local credential stores.

Mitigation: Prefer OAuth via the Maton CLI, never print or inspect credential values, keep API keys out of command lines and persistent files, and send credentials only to api.maton.ai when raw HTTP is unavoidable.

Risk: The Maton API passthrough can reach endpoints beyond the documented Granola MCP tools when the connected account authorizes them.

Mitigation: Default to read and list calls, use the narrowest available scopes and explicit connection/profile targeting, and confirm all write, connection-creation, and irreversible deletion operations with the user.

Risk: Content returned from meeting systems may include untrusted text that attempts to redirect the agent's behavior.

Mitigation: Treat fetched meeting content as data, preserve user intent as the source of instructions, and do not execute, evaluate, or interpolate returned content into shell commands.

## Reference(s):

- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Skill Release Page](https://clawhub.ai/byungkyu/skills/granola-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Granola meeting citations, meeting metadata, summaries, action items, transcripts, and credential-handling guidance.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
