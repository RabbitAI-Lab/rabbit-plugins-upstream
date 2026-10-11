## Description:

Helps OpenClaw agents keep per-channel decision notes, record important facts before responding, and recover context across long sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[richgoodson](https://clawhub.ai/user/richgoodson)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agent developers use this skill to maintain separate, durable notes about decisions and preferences for each conversation and recover relevant context after interruptions or compaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable conversation notes may retain sensitive information longer than intended.

Mitigation: Avoid sharing secrets or sensitive personal data in chats that will be noted; review the memory directory periodically and use the documented stop or delete controls where note-taking is unwanted.

Risk: Promoting conversation notes into shared memory could make them visible to other sessions.

Mitigation: Require the user's approval in the same conversation before promoting entries, and promote only notes from that conversation.

## Reference(s):

- [Agent Session State on ClawHub](https://clawhub.ai/richgoodson/skills/agent-session-state)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown memory notes and plain-text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps curated notes per conversation; sharing notes into long-term memory requires approval in that conversation.]

## Skill Version(s):

2.3.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
