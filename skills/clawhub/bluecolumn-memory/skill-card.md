## Description:

Give AI agents persistent semantic memory using the BlueColumn API for storing, recalling, and searching notes, conversations, documents, audio, and workflow context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect agents to BlueColumn memory so they can store selected durable context and recall it in later sessions. It supports REST and MCP-style workflows for remembering text, documents, audio URLs, preferences, decisions, and session summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content may be sent to BlueColumn for persistent searchable memory.

Mitigation: Require explicit user confirmation before storing transcripts, documents, sensitive personal data, or session summaries, and store only content the user wants remembered.

Risk: API keys can be exposed through plaintext notes or command-line usage.

Mitigation: Prefer a platform secret store, avoid storing keys in TOOLS.md, and avoid passing live keys directly on command lines.

Risk: Using the optional MCP package introduces package supply-chain review needs.

Mitigation: Pin and review the MCP package before running it in an agent environment.

## Reference(s):

- [BlueColumn API Reference](references/api.md)
- [BlueColumn Quickstart](https://bluecolumn.ai/docs/quickstart?utm_source=clawhub&utm_medium=skill&utm_campaign=bluecolumn-memory)
- [BlueColumn](https://bluecolumn.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST examples, endpoint field names, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples and user-facing reminders about consent, secrets, and selected memory storage.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
