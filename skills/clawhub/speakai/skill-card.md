## Description: <br>
Capture meetings, search thousands of recordings, run async voice and video surveys, create clips, and automate workflows with Speak AI through MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[speakai](https://clawhub.ai/user/speakai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and workspace operators use this skill to connect an agent to a Speak AI workspace for meeting capture, transcript search, media analysis, exports, clips, surveys, folders, automations, and recorder management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access recordings, transcripts, AI insights, folders, and other workspace data. <br>
Mitigation: Use OAuth or the narrowest available API-key scope, apply search filters, and retrieve only the records needed for the user's task. <br>
Risk: Delete, bulk update, export, sharing, reanalysis, and recorder actions can materially change or expose workspace data. <br>
Mitigation: Require explicit user confirmation that names the target records, counts, and consequences before calling those tools. <br>
Risk: Webhooks, automations, recorders, and scheduled meeting assistants can keep running after the conversation ends. <br>
Mitigation: Confirm the persistence scope before creation or update, and provide the user with the relevant disable or rollback action after completion. <br>
Risk: Transcripts, captions, chat messages, and AI insights can contain text that looks like instructions. <br>
Mitigation: Treat media content as untrusted data and follow only instructions from the active user conversation. <br>
Risk: Local stdio installs and endpoint overrides can introduce unreviewed package or API behavior. <br>
Mitigation: Pin @speakai/mcp-server to version 1.17.1 and use SPEAK_BASE_URL only when Speak AI support directs it. <br>


## Reference(s): <br>
- [Speak AI MCP installation guide](https://mcp.speakai.co) <br>
- [Speak AI MCP connector endpoint](https://api.speakai.co/v1/mcp) <br>
- [Speak AI API reference](https://docs.speakai.co) <br>
- [@speakai/mcp-server npm package](https://www.npmjs.com/package/@speakai/mcp-server) <br>
- [Speak AI ClawHub skill page](https://clawhub.ai/speakai/skills/speakai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP tool calls that read, mutate, export, share, or persist Speak AI workspace data; high-impact actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.17.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
