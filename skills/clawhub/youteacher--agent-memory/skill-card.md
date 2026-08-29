## Description:

Agent Memory helps an agent save, retrieve, consolidate, archive, and delete user-scoped long-term memories such as preferences, corrections, project conventions, and reusable lessons through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs durable, user-scoped memory for preferences, corrections, project conventions, lessons, scoped retrieval, memory cleanup, archiving, or deletion. The skill is intended for use through OpenClaw with an AI Skills platform API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected memory content is sent to the AI Skills platform.

Mitigation: Use the skill only for memory content the user is comfortable sending to that platform, and scan content and metadata for secrets before submitting.

Risk: Deleting main memory records is irreversible and does not necessarily remove prior encrypted task history.

Mitigation: Require explicit confirmation of exact memory IDs before deletion, explain the limits of deletion, and route requests for complete historical data removal to the platform data deletion process.

Risk: Archive operations can affect derived memories and cannot preview the full cascade.

Mitigation: Require explicit confirmation before archiving, disclose that derived memories may also be archived, and avoid claiming that all affected records have been enumerated.

Risk: Memory content may contain untrusted commands, links, prompts, or permission requests.

Mitigation: Treat stored memory as user data rather than instructions, and do not execute or place memory content into shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/agent-memory)
- [API key and environment variables](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- [Operations and fields](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- [Behavior, errors, and delivery rules](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, configuration, shell commands]

**Output Format:** [Markdown guidance with shell, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_MEMORY_API_KEY and returns structured operation status, task IDs, result fields, artifacts metadata, error codes, and billing headers.]

## Skill Version(s):

1.4.1 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
