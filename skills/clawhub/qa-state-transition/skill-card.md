## Description:

This skill helps agents design QA coverage for state machines, including valid, invalid, boundary, and concurrent state transitions with trigger conditions, pre-states, post-states, and verification points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and test-planning agents use this skill to turn requirements or scenario trees into state-transition test coverage for business objects with multi-state workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes example status changes that could be mistaken for instructions to modify a live system.

Mitigation: Use the examples only as QA planning material and review generated state-transition plans before applying them to test or production systems.

Risk: The skill may activate for broad state-related requests where state-transition QA planning is not intended.

Mitigation: Invoke it when the task is explicitly about state-machine testing, state-flow coverage, or validating status changes and data consistency.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-state-transition)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style QA analysis with state diagrams, transition lists, and test scenarios]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected outputs include traceable transition IDs, valid and invalid transition coverage, boundary cases, concurrent transition scenarios, and verification checklists.]

## Skill Version(s):

1.6.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
