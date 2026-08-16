## Description:

Connect an agent to Speak AI's MCP server to transcribe and analyze recordings, search workspace media, ask questions across transcripts and insights, create clips and exports, run surveys, schedule meeting assistants, and manage workspace resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and workspace operators use this skill to connect agents to Speak AI, select the right MCP tools, and run common recording, transcript, search, meeting, survey, export, automation, webhook, dashboard, and team-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected agent may read recordings, transcripts, insights, and workspace metadata allowed by the user's Speak AI account.

Mitigation: Connect only to the intended workspace, review account permissions, and prefer OAuth so the user can authorize and revoke access without handling an API key.

Risk: Meeting recording, share links, webhooks, automations, deletes, exports, and group changes can affect other users or persist after the chat.

Mitigation: Confirm the action, exact ids, affected counts, and consequences before execution, and provide the relevant undo or cancellation step after a lasting change.

Risk: API keys and alternate base URLs can expose workspace access or route traffic somewhere unexpected.

Mitigation: Keep API keys private, rotate them if exposed, and use the documented default Speak AI API endpoint unless Speak AI support explicitly instructs otherwise.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/speakai/skills/speakai)
- [Speak AI MCP Documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP Setup Guide](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP Tool Reference](https://docs.speakai.co/mcp/tools/)
- [Upload and Analyze Tool Documentation](https://docs.speakai.co/mcp/tools/media/upload_and_analyze/)
- [Ask AI Chat Tool Documentation](https://docs.speakai.co/mcp/tools/magic-prompt/ask_ai_chat/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup steps, tool-selection guidance, workflow instructions, and confirmation guidance for sensitive actions.]

## Skill Version(s):

1.21.1 (source: server evidence release.version and metadata server-version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
