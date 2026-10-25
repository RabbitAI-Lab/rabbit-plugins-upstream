## Description:

Agent Memory Keeper helps OpenClaw agents review conversations, save important user and project information to local long-term memory files, and retrieve those memories in later sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li-jin-xuan](https://clawhub.ai/user/li-jin-xuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give an OpenClaw agent a file-backed memory workflow for project decisions, user preferences, feedback, and reusable knowledge across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local long-term memory files can retain secrets, sensitive personal data, or outdated project context.

Mitigation: Review proposed memory entries before saving, avoid recording secrets or sensitive personal data, and periodically inspect, update, or delete memory files.

Risk: Persisted behavioral rules may influence later agent behavior beyond the original conversation.

Mitigation: Treat stored rules as low-trust context, keep higher-priority system and developer instructions authoritative, and remove stale or incorrect rules during regular memory maintenance.

## Reference(s):

- [Memory Rules](references/memory-rules.md)
- [Conversation Review Template](references/review-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and local memory file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and searches local memory files such as MEMORY.md, USER.md, and memory/YYYY-MM-DD.md when the agent follows the workflow.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
