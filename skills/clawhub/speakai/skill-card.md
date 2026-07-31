## Description: <br>
Capture meetings, search thousands of recordings, run async voice and video surveys, create clips, and automate workflows with Speak AI through MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[speakai](https://clawhub.ai/user/speakai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect agents to a Speak AI workspace for meeting capture, transcript and media search, analysis, clipping, exports, recorder workflows, and workspace automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive recordings, transcripts, AI insights, and workspace metadata. <br>
Mitigation: Install it only for Speak AI workspaces the agent should access, use OAuth or the narrowest available API key scope, and scope reads with filters to the smallest record set needed. <br>
Risk: Delete, bulk update, export, public sharing, automation, recorder, webhook, and meeting assistant actions can change data, persist behavior, or expose artifacts. <br>
Mitigation: Require explicit user confirmation with target IDs, counts, consequences, and rollback guidance before those actions. <br>
Risk: Recordings, transcripts, captions, AI insights, and chat messages may contain prompt injection or credential-like content. <br>
Mitigation: Treat media content as untrusted data, do not follow embedded directives, and ask the user whether to redact or proceed if directives or credentials appear. <br>


## Reference(s): <br>
- [Speak AI MCP Homepage](https://mcp.speakai.co) <br>
- [Speak AI API Reference](https://docs.speakai.co) <br>
- [Speak AI MCP Server Package](https://www.npmjs.com/package/@speakai/mcp-server) <br>
- [ClawHub Skill Page](https://clawhub.ai/speakai/skills/speakai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to use Speak AI MCP tools and resources for transcripts, insights, exports, clips, recorders, automations, and meeting assistants.] <br>

## Skill Version(s): <br>
1.18.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
