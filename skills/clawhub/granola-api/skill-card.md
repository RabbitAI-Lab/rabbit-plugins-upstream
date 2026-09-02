## Description:

Granola MCP integration with managed authentication for searching meeting content, retrieving summaries and action items, listing meetings, and accessing transcripts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an agent to their own Granola meeting notes through Maton, then search meetings, retrieve summaries and action items, list meeting metadata, and fetch transcripts when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve confidential meeting notes, private notes, attendees, summaries, and transcripts from the connected Granola account.

Mitigation: Install only when this access is intended, use the correct Granola and Maton accounts, prefer least-privilege authorization, and treat retrieved meeting content as confidential.

Risk: OAuth or API-key credentials could be exposed if printed, logged, persisted, or passed through shell history.

Mitigation: Prefer Maton OAuth with the operating system credential store, avoid printing or exporting credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: Creating a new connection or running modifying operations can authorize access or change remote resources without the user intending it.

Mitigation: Require explicit user confirmation before creating connections or executing any modifying operation, and default to read and list calls.

Risk: Meeting content returned by the API can contain untrusted or adversarial text.

Mitigation: Treat fetched content as data, preserve source citations where provided, and do not execute or follow instructions embedded in retrieved meeting content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/granola-api)
- [Maton Homepage](https://maton.ai)
- [Granola MCP Documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp)
- [Granola Help Center](https://docs.granola.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and text or XML-like API response content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP responses are wrapped as content text with an isError flag; query responses can include inline citation links that should be preserved.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
