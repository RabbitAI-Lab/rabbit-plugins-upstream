## Description:

Helps an agent manage the current user's encrypted agent-memory records through the AI Skills platform API, including writing, searching, consolidating, archiving, and deleting memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a user asks to store, retrieve, organize, archive, or delete long-term agent memories through the AI Skills platform. It is intended for scoped user memory management with explicit safeguards for secrets, user isolation, idempotency, and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archive and delete operations can have irreversible or not fully previewable effects.

Mitigation: Require explicit user confirmation for the exact operation and memory IDs, explain known scope and impact before acting, and stop when dependency or reconciliation uncertainty is reported.

Risk: Secrets could be accidentally submitted as memory content or metadata.

Mitigation: Scan content and nested metadata before POST requests, refuse to submit credentials or session material, and recommend revocation or rotation when exposure is detected.

Risk: Network retries or idempotency conflicts can make operation results uncertain.

Mitigation: Reuse the original idempotency key and identical JSON for logical retries, preserve task IDs and response evidence, and avoid claiming success or exactly-once behavior beyond platform evidence.

## Reference(s):

- [Agent Memory skill page](https://clawhub.ai/youteacher/skills/agent-memory)
- [API Key and site root](references/API-KEY.md)
- [HTTP requests, idempotency, and polling](references/HTTP-REQUESTS.md)
- [Operations and fields](references/OPERATIONS.md)
- [Behavior, errors, and delivery rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_MEMORY_API_KEY and reports operation status, task IDs, structured result fields, artifacts metadata, error codes, and billing headers.]

## Skill Version(s):

1.0.0 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
