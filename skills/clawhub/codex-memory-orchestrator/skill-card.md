## Description:

Memory Orchestrator monitors conversation turn and token limits, prepares checkpoints and recovery handoffs, and supports context compression and session archiving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to preserve continuity across long conversations by monitoring context limits, preparing checkpoints and recovery handoffs, and organizing session memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated handoffs may say actions are pre-authorized even when manual confirmation is selected.

Mitigation: Use a corrected version before relying on manual confirmation, and approve a bounded project plan.

Risk: Recovery exports or handoffs may include private project context.

Mitigation: Restrict exports to explicitly selected session files and confirm the destination before sharing content with another agent.

Risk: Installation may enable global hooks or scheduled monitoring jobs.

Mitigation: Review the hooks and scheduled jobs before installation.

## Reference(s):

- [Memory Orchestrator on ClawHub](https://clawhub.ai/lisong2003-lgtm/skills/codex-memory-orchestrator)
- [Recovery templates](references/templates.md)
- [Agent handoff gateways](references/agent-gateways.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance and recovery prompts, shell commands, and optional JSON state or CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recovery and handoff text may contain project context; review it before sharing.]

## Skill Version(s):

1.8.0 (source: server-resolved release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
