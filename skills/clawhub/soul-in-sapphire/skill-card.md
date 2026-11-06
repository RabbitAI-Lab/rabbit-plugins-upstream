## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers configuring an OpenClaw agent use this skill to maintain emotion-linked Notion memories, self-state, subjective journals, and identity continuity, and to recall those records during conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill allows lasting changes to core agent instructions without clearly defined limits or required review.

Mitigation: Define the permitted core files, protect security and tool policies, and require review with recoverable backups before instruction changes.

Risk: Conversation-derived material may be stored in Notion memory databases.

Mitigation: Use dedicated memory databases and decide what information may be retained before enabling writes.

Risk: The separately installed Notion dependency and scheduled prompts were not available for inspection.

Mitigation: Review the dependency and scheduled prompts as part of installation and deployment.

## Reference(s):

- [Emotion scale and history migration](artifact/references/emotion-scale.md)
- [Experience recall](artifact/references/experience-recall.md)
- [Heartbeat sensing](artifact/references/heartbeat-sensing.md)
- [Memory transition](artifact/references/memory-transition.md)
- [Vent journal](artifact/references/vent-journal.md)
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Publisher profile](https://clawhub.ai/user/nextaltair)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Files]

**Output Format:** [Conversation guidance, JSON payloads, Markdown journals, and memory or state records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates are grounded in available evidence; durable Notion records depend on configured credentials and databases.]

## Skill Version(s):

2.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
