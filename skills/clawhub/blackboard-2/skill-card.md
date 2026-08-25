## Description:

Typed multi-model workspace with kitchen-shift ownership, resource, hazard, protected-target, and next-action handovers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Blackboard to coordinate multi-model task handoffs through a typed, auditable JSON board instead of an unstructured notes blob. It helps preserve current state, ownership, constraints, evidence, failures, hazards, and the next bounded action across agent shifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may persist sensitive or inappropriate task state in local JSON board files.

Mitigation: Keep boards only in the intended project or work area, review board contents before routing work between agents, and avoid recording private reasoning.

Risk: A model could treat user approvals or user decisions as model-selectable strings.

Mitigation: Bind user/* identities and user provenance to authenticated inbound users in the calling environment before accepting decisions or destructive-action approvals.

Risk: Agents may act on stale, unsafe, or protected targets during handoff.

Mitigation: Run validate before each hop, use guard before actions, record hazards and DO_NOT_TOUCH targets, and require independent PASS evidence before completion.

## Reference(s):

- [Blackboard schema](references/schema.md)
- [Three-model canary](references/canary.md)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/blackboard-2)
- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/blackboard)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, json]

**Output Format:** [Markdown guidance with shell commands that create, validate, and mutate local JSON board files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Board mutations are revisioned, locked, validated, written atomically, and backed up locally.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
