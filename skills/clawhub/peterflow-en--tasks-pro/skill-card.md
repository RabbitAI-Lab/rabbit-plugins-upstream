## Description:

Split a large change into phases that fresh implementers, reviewers and testers can pick up independently. Include ownership, handoff inputs and cumulative acceptance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to turn a large change into independently executable phases with clear ownership, dependencies, handoff artifacts, acceptance checks, and cumulative integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The host runtime's enforcement of this skill's tool permissions could not be verified.

Mitigation: Before installing, confirm the runtime's permission controls and whether the skill's tool scope is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/peterflow-en/skills/tasks-pro)
- [Phase task template](assets/tasks.md)
- [Dependency checker](scripts/check_dependencies.py)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown task plan with phase and task IDs, dependencies, ownership, handoffs, and acceptance checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dependency checker can validate explicit dependencies and final-phase coverage for standard-format plans.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
