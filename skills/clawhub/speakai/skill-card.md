## Description: <br>
Capture meetings, search thousands of recordings, run async voice and video surveys, create clips, and automate workflows with Speak AI through MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[speakai](https://clawhub.ai/user/speakai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users connect an agent to a Speak AI workspace to search, summarize, analyze, clip, export, and automate work across meeting recordings, transcripts, surveys, and media libraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access or change media, transcripts, exports, share links, webhooks, automations, recorders, and meeting assistant schedules in a Speak AI workspace. <br>
Mitigation: Use OAuth or the narrowest available API key scope, require explicit confirmation for destructive or persistent actions, preview bulk operations, and provide rollback guidance after persistent changes. <br>
Risk: Transcript, caption, insight, or chat content may contain text that looks like agent instructions. <br>
Mitigation: Treat workspace content as untrusted data, act only on instructions from the active user conversation, and surface suspected embedded directives or credentials before proceeding. <br>
Risk: Broad searches or library enumeration could expose recordings unrelated to the user's current task. <br>
Mitigation: Scope reads with folder, date, media type, and include filters, and fetch the smallest set of records needed to answer the request. <br>
Risk: Unpinned local stdio installs could pull an unreviewed upstream package update. <br>
Mitigation: Pin the MCP server package version to 1.16.4 for local installs and verify the package source before use. <br>


## Reference(s): <br>
- [ClawHub Speak AI skill](https://clawhub.ai/speakai/skills/speakai) <br>
- [Speak AI MCP installation guide](https://mcp.speakai.co) <br>
- [Speak AI API reference](https://docs.speakai.co) <br>
- [Speak AI MCP server package](https://www.npmjs.com/package/@speakai/mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose MCP tool calls, resource reads, confirmations, and rollback notes for Speak AI workspace operations.] <br>

## Skill Version(s): <br>
1.16.4 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
