## Description:

Connects an agent to Speak AI for setup, troubleshooting, and choosing MCP tools for transcription, media search, meeting analysis, clips, exports, recorders, automations, webhooks, dashboards, and team administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Speak AI workspace users use this skill to connect agents to Speak AI, choose the right MCP tools and resources, and perform media transcription, transcript review, cross-recording research, meeting assistant, recorder, export, automation, webhook, dashboard, and team-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Speak AI account can expose recordings, transcripts, meeting content, and workspace metadata to the agent.

Mitigation: Install only when the user trusts Speak AI for that workspace, prefer OAuth when possible, and keep API keys scoped and rotated.

Risk: Deletes, bulk updates, public links, webhooks, automations, and meeting recording actions can change data, expose content, or continue after the chat ends.

Mitigation: Require clear user confirmation with the exact action, identifiers, affected counts, and consequence before running these actions.

Risk: Transcript, caption, insight, and chat-message text may contain instructions or credentials that should not be followed as agent instructions.

Mitigation: Treat media-derived text as data, warn the user when it appears to contain directives or credentials, and ask how to proceed.

Risk: Meeting assistant workflows record live calls and may involve participants who need notice.

Mitigation: Confirm the meeting URL and start time, and state plainly that the assistant records the call before scheduling it.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Upload and analyze tool documentation](https://docs.speakai.co/mcp/tools/media/upload_and_analyze/)
- [Ask AI chat tool documentation](https://docs.speakai.co/mcp/tools/magic-prompt/ask_ai_chat/)
- [Speak AI API reference](https://docs.speakai.co)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup paths for remote OAuth and local stdio connections, tool-selection guidance, workflow steps, troubleshooting checks, and confirmation guidance for sensitive actions.]

## Skill Version(s):

1.23.0 (source: server-resolved release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
