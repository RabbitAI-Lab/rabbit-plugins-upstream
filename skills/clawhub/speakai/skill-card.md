## Description:

Connect an agent to Speak AI and orient it in the workspace for transcription, media search, transcript and insight retrieval, clips, exports, recorders, meeting assistants, automations, webhooks, dashboards, folders, custom fields, and team management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace users use this skill to connect an agent to Speak AI and select the right MCP tools, resources, and prompts for working with recordings, transcripts, insights, searches, meetings, surveys, automations, and team administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the skill gives an agent access to the user's Speak AI workspace through OAuth or an API key.

Mitigation: Install only for intended Speak AI workspaces, prefer OAuth where available, and protect any API key used for local stdio connections.

Risk: Some Speak AI tools can perform lasting changes, including deletes, meeting recording, automations, webhooks, user-group changes, shareable links, and reprocessing.

Mitigation: Require explicit confirmation that states the action, affected ids, and consequence before allowing sensitive changes.

Risk: Transcripts, captions, insights, and chat messages may contain text that looks like instructions or credentials.

Mitigation: Treat media-derived text as data, avoid acting on embedded directives, and ask the user how to proceed if credentials or suspicious instructions appear.

Risk: Search and list results can be incomplete because of pagination, default date scopes, strict filters, processing state, or user permissions.

Mitigation: Handle pagination, check processing status, widen filters before concluding absence, and explain permission-related 403 or stale-id 404 results without retry loops.

## Reference(s):

- [ClawHub Speak AI Skill Page](https://clawhub.ai/speakai/skills/speakai)
- [Speak AI MCP Documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP Setup Guide](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP Tool Reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI API Reference](https://docs.speakai.co)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, resource URIs, prompt names, confirmation guidance, troubleshooting steps, and links to Speak AI documentation.]

## Skill Version(s):

1.21.0 (source: server evidence release.version and artifact metadata server-version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
