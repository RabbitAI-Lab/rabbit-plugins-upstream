## Description:

Helps agents connect to Speak AI and use workspace tools to transcribe, search, analyze, and manage recordings and related content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Speak AI can connect an agent to their workspace to transcribe media, find and summarize recordings, export results, and manage meeting, survey, and automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if pasted into chats or committed to files.

Mitigation: Prefer OAuth when available; otherwise store the key using the supported client or secret mechanism.

Risk: Deletes, bulk changes, meeting recording, and persistent automations can affect workspace data or other people.

Mitigation: Confirm the exact action and affected records with the user before proceeding.

Risk: Shared links, webhooks, and exports can expose workspace content beyond its intended audience.

Mitigation: Review recipients and link visibility, and obtain user confirmation before sharing or exporting.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP authentication](https://docs.speakai.co/mcp/authentication)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI skill release](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transcripts, summaries, and links returned by Speak AI tools.]

## Skill Version(s):

1.28.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
