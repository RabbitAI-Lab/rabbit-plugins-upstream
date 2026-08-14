## Description:

Design a multi-agent team that actually routes work. Pick roles by what they refuse, wire reporting lines, bound hand-offs, and place human gates, before writing any orchestration code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[delasy](https://clawhub.ai/user/delasy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design or repair multi-agent team structures before writing orchestration code. It helps define agent roles, refusal boundaries, reporting lines, hand-off limits, and human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A resulting org chart could give agents broad write access, memory, or third-party tool authority without appropriate human gates.

Mitigation: Review tool authority per tool and require human approval for costly, external, or hard-to-undo actions.

Risk: Poorly bounded delegation can create loops, uncontrolled fan-out, or concurrent writes to shared state.

Mitigation: Enforce a tree-shaped routing structure, cap fan-out and chain depth, and serialize writers on shared mutable resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/delasy/skills/agent-org-chart)
- [Org chart feature reference](https://aldena.ai/features/org-chart)
- [Agent archetype reference](https://aldena.ai/features/agents)
- [Failure modes](reference/failure-modes.md)
- [Role archetypes](reference/role-archetypes.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown design specification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a written org chart spec with roles, reporting edges, hand-off caps, and tool approval policies.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
