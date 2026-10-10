## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to retain and recall emotion-linked experiences, track an agent's self-state, write subjective journals, and maintain identity continuity across conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private emotional memories, self-state, and journals may be stored in Notion and local agent memory files.

Mitigation: Install only if this storage is intended; restrict access to the Notion integration and local memory files.

Risk: Notion credentials and database identifiers may be exposed if shared in conversation or logs.

Mitigation: Keep tokens and database IDs out of chat and logs, and use a least-privilege Notion integration.

Risk: Scheduled checks and ambient recall can stage or revisit sensitive context unexpectedly.

Mitigation: Review cron and heartbeat setup separately; set SIS_AMBIENT_RECALL=0 to disable ambient recall staging when unwanted.

## Reference(s):

- [Soul in Sapphire on ClawHub](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Emotion scale and migration](artifact/references/emotion-scale.md)
- [Experience recall](artifact/references/experience-recall.md)
- [Heartbeat sensing](artifact/references/heartbeat-sensing.md)
- [Memory transition](artifact/references/memory-transition.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational text and structured memory, state, and journal records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and Notion access for backed memory operations; supports local state files.]

## Skill Version(s):

2.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
