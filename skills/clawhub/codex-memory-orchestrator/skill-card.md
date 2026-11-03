## Description:

Helps agents preserve context across long conversations with memory retrieval, turn and token monitoring, checkpoints, recovery packages, and handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to keep long-running conversations resumable, monitor active dialog thresholds, and create checkpoints or recovery packages for continuing work in a new conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual mode may not preserve approval across every generated step or handoff.

Mitigation: Review each generated step yourself; manual mode alone is insufficient until using a corrected version that preserves approval throughout handoffs.

Risk: Monitoring, transcript exports, or cross-agent transfers may exceed approved conversation privacy boundaries.

Mitigation: Limit monitoring and exports to approved conversations, explicitly choose any persistent hooks or schedules, and review transcript exports and transfers before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/codex-memory-orchestrator)
- [Handoff gateway guide](references/agent-gateways.md)
- [Recovery package templates](references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, JSON, Guidance]

**Output Format:** [Markdown recovery packages, JSON state and handoff data, and shell or Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local state, checkpoint, and recovery files.]

## Skill Version(s):

1.9.2 (source: SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
