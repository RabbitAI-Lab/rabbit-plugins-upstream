## Description:

Helps agents save, search, consolidate, archive, and delete user-scoped long-term memories such as preferences, corrections, project conventions, and reusable lessons through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a user explicitly asks an agent to remember, retrieve, organize, archive, or delete long-term memory through a user-scoped API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and retrieves long-term memory through an external AI Skills account.

Mitigation: Install it only when that account and API endpoint are intended for the user's memory workflow, and confirm the endpoint before configuring the API key.

Risk: Sensitive personal data or credentials could be submitted as memory content or metadata.

Mitigation: Scan content and metadata before POST requests, do not submit detected secrets, and advise credential rotation when exposure is identified.

Risk: Archive and delete operations can have durable effects; archive is not reversible through the API and delete does not erase prior encrypted task-history copies.

Mitigation: Require explicit user confirmation for exact memory IDs and clearly report limits of archive, delete, and retained task history.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/agent-memory)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key and Environment](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- [HTTP Requests, Idempotency, and Polling](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- [Operations and Fields](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- [Behavior, Errors, and Delivery Rules](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP requests, and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_MEMORY_API_KEY and uses user-scoped memory operations with idempotency keys and bounded polling.]

## Skill Version(s):

1.5.2 (source: server release metadata and packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
