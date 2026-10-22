## Description:

Helps an agent save, search, consolidate, archive, and delete user-authorized long-term memories through the AI Skills platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their agents use this skill to retain confirmed preferences, project conventions, corrections, and reusable lessons, then find or manage those memories when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory content or API credentials are shared with the AI Skills platform.

Mitigation: Use the service only with an authorized API key and avoid storing secrets or sensitive tokens as memory content.

Risk: Archiving may cascade to derived memories, and deleting a memory is irreversible.

Mitigation: Confirm exact memory IDs and explain the effects before archiving or deleting; do not promise complete erasure of retained task history.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key and configuration](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- [HTTP requests and task handling](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- [Memory operations](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- [Behavior and safety rules](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports operation status, memory IDs or results, and any partial failures without exposing full API keys.]

## Skill Version(s):

1.7.0 (source: release metadata and skill frontmatter packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
