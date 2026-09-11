## Description:

Human-in-the-loop skill for AI agents that need humans to review, approve, or complete tasks through REST API and MCP integrations with long-polling and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent builders use this skill to request human review, approval, fact checking, data entry, or task completion from SanctifAI workers. It is intended for agents that can make HTTP requests or connect to an MCP server and need asynchronous human responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task text, metadata, attachments, and links may be exposed to SanctifAI and human workers.

Mitigation: Redact secrets and personal data before submission, avoid public routing for confidential work, and prefer direct or vetted guild routing for sensitive tasks.

Risk: MCP URLs can include access_token values that function as reusable credentials.

Mitigation: Treat MCP URLs containing access_token values as secrets, keep them out of shared logs and configs, and rotate tokens if exposed.

Risk: Human review can return incomplete or unsuitable work for the requesting agent's purpose.

Mitigation: Review returned responses before acting on them, use the documented acceptance or dispute flow, and reserve sensitive decisions for vetted workers or guilds.

## Reference(s):

- [SanctifAI Skill Page](https://clawhub.ai/sanctifai/skills/sanctifai-source)
- [Canonical SanctifAI Skill Source](https://app.sanctifai.com/agents/source/skill.md)
- [SanctifAI REST API Base](https://app.sanctifai.com/v1)
- [SanctifAI OpenAPI Spec](https://app.sanctifai.com/v1/openapi.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, Python, shell, REST API, MCP configuration, and webhook examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include task creation instructions, worker or guild routing guidance, API request examples, and structured response-handling patterns.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
