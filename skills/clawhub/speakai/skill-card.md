## Description:

Guides agents in connecting to Speak AI and using workspace tools to transcribe, search, analyze, and manage recordings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speakai](https://clawhub.ai/user/speakai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace users and developers use this skill to connect an agent to Speak AI, find and analyze recordings and transcripts, and manage related workspace workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed in shared chats or logs.

Mitigation: Prefer OAuth where available; do not paste real API keys into shared chats or logs.

Risk: Deletes, bulk updates, and persistent automations or webhooks can make lasting workspace changes.

Mitigation: Review the requested action and affected records, then obtain explicit approval before proceeding.

Risk: Meeting recording and shareable links may expose other people's content.

Mitigation: Confirm recording and sharing requests with the user before enabling them.

## Reference(s):

- [Speak AI MCP documentation](https://docs.speakai.co/mcp)
- [Speak AI MCP setup](https://docs.speakai.co/mcp/setup/)
- [Speak AI MCP tool reference](https://docs.speakai.co/mcp/tools/)
- [Speak AI skill on ClawHub](https://clawhub.ai/speakai/skills/speakai)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Text]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and responses depend on the connected user's workspace permissions.]

## Skill Version(s):

1.39.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
