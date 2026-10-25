## Description:

Coordinates long-conversation memory retrieval, monitoring, handoffs, recovery packages, checkpoints, compression, and archiving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers use the skill to preserve useful context across long-running agent conversations, prepare recovery packages, and continue work in a new conversation. It also supports project checkpoints and conversation archiving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual approval settings may not reliably constrain automated project handoffs.

Mitigation: Avoid automatic project execution until manual-mode handoffs preserve approval requirements; review approval behavior before enabling automation.

Risk: Conversation access may exceed the intended project or conversation scope.

Mitigation: Require exact conversation and project boundaries, and confirm monitoring is limited to the intended active conversations.

Risk: Scheduled jobs or global agent-rule changes may have persistent effects.

Mitigation: Explicitly approve scheduled jobs and global rule changes, and establish how to remove them before setup.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/memory-orchestrator)
- [Recovery package templates](references/templates.md)
- [Agent handoff gateways](references/agent-gateways.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance, Configuration]

**Output Format:** [Recovery packages, checkpoints, handoff prompts, and memory summaries, primarily in Markdown or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local state, recovery, and archive files.]

## Skill Version(s):

1.9.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
