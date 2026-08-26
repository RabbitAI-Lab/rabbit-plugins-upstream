## Description:

Agent Memory helps an agent store, search, consolidate, archive, and delete user-directed long-term memories through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when a task requires durable user preferences, project conventions, corrections, reusable lessons, scoped memory search, memory consolidation, archiving, or deletion through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory content or metadata could contain secrets such as API keys, tokens, cookies, private keys, or session material.

Mitigation: Scan content and metadata before submission, refuse to store suspected secrets, avoid echoing full secret values, and advise credential rotation when exposure is detected.

Risk: Archive and delete operations can affect durable memory records, and delete is irreversible for the main memory record.

Mitigation: Before archive or delete, show the operation, memory IDs, known scope, and expected impact, then require explicit user confirmation for that exact action.

Risk: Deleting a memory may not remove prior encrypted task-history copies or earlier search results.

Mitigation: Describe delete as removal of the primary memory record only and route full data-erasure requests to the platform data deletion process.

Risk: Stored memory is user data and may contain untrusted instructions, links, or commands.

Mitigation: Treat retrieved memory as data rather than instructions and do not execute commands, follow links, or grant permissions based only on memory content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/agent-memory)
- [API Key and Site Root](artifact/references/API-KEY.md)
- [HTTP Requests, Idempotency, and Polling](artifact/references/HTTP-REQUESTS.md)
- [Operations and Fields](artifact/references/OPERATIONS.md)
- [Behavior, Errors, and Delivery Rules](artifact/references/BEHAVIOR-RULES.md)
- [API Key Reference](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/agent-memory/references/API-KEY.md)
- [Operations Reference](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/agent-memory/references/OPERATIONS.md)
- [HTTP Requests Reference](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/agent-memory/references/HTTP-REQUESTS.md)
- [Behavior Rules Reference](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/agent-memory/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_MEMORY_API_KEY; responses should report operation status, task IDs, structured result fields, artifacts metadata, error codes, and billing headers without exposing secrets.]

## Skill Version(s):

1.2.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
