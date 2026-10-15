## Description:

Guides agents through connecting to Speak AI and using workspace tools for transcription, search, analysis, exports, surveys, and meeting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users connect to a Speak AI workspace to transcribe and analyze recordings, search media, export results, and manage surveys and meeting assistants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure when using a local connection.

Mitigation: Prefer OAuth where supported and treat API keys as secrets.

Risk: Destructive or broad changes to workspace data.

Mitigation: Review the exact records and obtain clear user confirmation before deletes or bulk updates.

Risk: Unintended sharing or persistent actions through links, webhooks, automations, or meeting recordings.

Mitigation: Confirm scope and audience before creating public links or enabling ongoing workflows or meeting capture.

## Reference(s):

- [Speak AI on ClawHub](https://clawhub.ai/speakai/skills/speakai)
- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP authentication](https://docs.speakai.co/mcp/authentication)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool-specific responses depend on the connected workspace and user permissions.]

## Skill Version(s):

1.35.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
