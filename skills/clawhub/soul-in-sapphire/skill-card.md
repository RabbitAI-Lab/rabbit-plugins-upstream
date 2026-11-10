## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to maintain emotion-linked experience memories, current self-state, subjective journals, and identity continuity across conversations. It supports local state mirrors and authorized Notion recall and writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags broad Notion access and core-context update behavior.

Mitigation: Review the Notion permissions and data capabilities before enabling writes, and keep core-context changes explicitly authorized and inspectable.

Risk: Installation guidance includes an unpinned command and self-update guidance.

Mitigation: Review and pin the release version before installation, and assess self-update guidance before following it.

Risk: The security scan inspected only 10 of 41 components, leaving other behavior unestablished.

Mitigation: Inspect the remaining components before relying on the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Emotion scale and persistence](references/emotion-scale.md)
- [Experience recall](references/experience-recall.md)
- [Heartbeat sensing](references/heartbeat-sensing.md)
- [Memory transition](references/memory-transition.md)
- [Vent journal](references/vent-journal.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON, Files, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Conversational text, Markdown journal entries, and JSON state or observation files; authorized Notion records when configured.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use OpenClaw memory tools, local workspace files, and configured Notion access.]

## Skill Version(s):

2.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
