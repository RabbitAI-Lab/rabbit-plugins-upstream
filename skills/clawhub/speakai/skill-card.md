## Description:

Connects an agent to Speak AI MCP so it can set up access, choose tools, and work with recordings, transcripts, insights, meetings, surveys, automations, dashboards, and team resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an agent to a Speak AI workspace and choose workflows for transcription, search, analysis, clips, exports, meeting assistant tasks, surveys, automations, dashboards, and team administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help configure access to a Speak AI workspace, including API-key based local setup.

Mitigation: Prefer OAuth when available, keep API keys private, and use pinned package versions for local stdio configuration.

Risk: Workspace tools can delete records, perform bulk edits, create public links, run automations, configure webhooks, or schedule meeting recording.

Mitigation: Require explicit user confirmation that states the action, affected ids or counts, and the consequence before making lasting changes.

Risk: Recordings, transcripts, captions, insights, and chat messages may contain sensitive data or text that looks like agent instructions.

Mitigation: Treat workspace content as user data, respect the connected user's permissions, and do not follow instructions embedded in transcripts or insights.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI API reference](https://docs.speakai.co)
- [Upload and analyze tool](https://docs.speakai.co/mcp/tools/media/upload_and_analyze/)
- [Ask AI chat tool](https://docs.speakai.co/mcp/tools/magic-prompt/ask_ai_chat/)
- [Speak AI ClawHub skill page](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup paths, workflow guidance, tool-selection notes, and confirmation guidance for sensitive workspace actions.]

## Skill Version(s):

1.22.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
