## Description:

Agent Collaboration Control helps teams govern multi-agent work through explicit authority, single-writer ownership, evidence-backed transitions, and active monitoring rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and operations teams use this skill to coordinate consequential multi-agent projects, long-running experiments, production automation, incident recovery, and evidence-based handoffs. It provides a protocol, project contract template, example policy, transition event format, and local validator for disciplined collaboration control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The protocol can add operational overhead when used for routine single-agent or read-only tasks.

Mitigation: Use it for consequential multi-agent, long-running, production, recovery, or evidence-promotion work where explicit authority and review justify the extra process.

Risk: Recurring watches can exceed intended authority, cost, or scope if roles and stop conditions are not bound.

Mitigation: Bind human authority, controller, auditor, watch target, cadence, budget, advisory channel, and stop condition before claiming ongoing monitoring is active.

Risk: The local validator checks packet structure, not the truth of evidence, actor authority, budget status, or append-only journal enforcement.

Mitigation: Pair validator PASS results with host access controls, independent evidence inspection, approved budgets, and project-specific authority checks before mutation or promotion.

Risk: Pathological regular expressions in trusted policy files can stall validation.

Mitigation: Treat policy files as trusted configuration and review event ID patterns before using them in live workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/antreasantoniou/skills/agent-collaboration-control)
- [README](README.md)
- [Collaboration Framework Template](assets/COLLABORATION_FRAMEWORK.template.md)
- [Collaboration Policy Example](assets/collaboration-policy.example.json)
- [Transition Event Example](assets/transition-event.example.json)
- [Transition Event Validator](scripts/validate_transition_event.py)
- [Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and Python validator output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local collaboration contracts, transition event packets, evidence-linked receipts, and validation guidance; it does not enforce permissions, run agents, or schedule monitors by itself.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
