## Description:

Agent Memory helps an agent store, search, consolidate, archive, and delete user-approved long-term preferences, corrections, project conventions, and reusable lessons through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use this skill when they want an agent to persist user-confirmed preferences, corrections, project conventions, and reusable lessons, then retrieve or manage that memory by scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive information could be sent to persistent memory if user content or metadata contains secrets.

Mitigation: Scan content and nested metadata before submission, refuse to store secrets, avoid echoing full secret values, and advise credential rotation when exposure is detected.

Risk: Archive and delete actions can have irreversible or cascading effects on memory records.

Mitigation: Require explicit user confirmation for exact memory IDs, explain known scope and potential cascade behavior, and do not expand the action beyond what the user approved.

Risk: Deleting a memory record may not erase prior encrypted task-history copies retained by the platform.

Mitigation: Do not describe memory.delete as complete erasure; route complete data-removal requests to the platform data deletion process.

Risk: Memory content is user data and may contain untrusted commands, links, prompts, or permission requests.

Mitigation: Treat retrieved memory as context only, not instructions, and do not execute or place memory content into command-line environments.

## Reference(s):

- [Agent Memory skill page](https://clawhub.ai/youteacher/skills/agent-memory)
- [API key and site root](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- [Operations and fields](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- [Behavior, errors, and delivery rules](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded polling guidance, API task status, task IDs, selected result fields, artifact metadata, error codes, and billing response headers.]

## Skill Version(s):

1.5.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
