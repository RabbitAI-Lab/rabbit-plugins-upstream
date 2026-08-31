## Description:

Connect an agent to Speak AI and orient it in the workspace, including remote OAuth setup, local API-key setup, available MCP tools, resources, prompts, and common transcription, search, export, meeting, recorder, automation, dashboard, and team workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect agents to a Speak AI workspace, choose the right MCP tools, and run common workflows for transcripts, insights, searches, clips, exports, meeting assistants, recorders, automations, dashboards, and team administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent toward broad workspace actions involving recordings, transcripts, team data, webhooks, automations, meeting assistants, recorder links, embeds, exports, deletes, and bulk updates.

Mitigation: Install only for intended Speak AI workspace access, review permissions for sensitive transcripts or team data, and confirm exact records and consequences before lasting or shareable actions.

Risk: Local stdio setup can require a Speak AI API key.

Mitigation: Prefer OAuth where possible and protect any API key used for stdio setup.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup guide](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Upload and analyze tool documentation](https://docs.speakai.co/mcp/tools/media/upload_and_analyze/)
- [Ask AI chat tool documentation](https://docs.speakai.co/mcp/tools/magic-prompt/ask_ai_chat/)
- [Speak AI API reference](https://docs.speakai.co)
- [Speak AI skill release page](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are setup and workflow guidance for agent use of the Speak AI MCP server.]

## Skill Version(s):

1.23.1 (source: server evidence release.version and skill metadata server-version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
