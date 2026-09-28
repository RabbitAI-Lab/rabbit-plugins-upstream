## Description:

Designs state-machine test cases for valid, invalid, boundary, and concurrent transitions, with checks for data consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to identify business-object states and design traceable tests for allowed, forbidden, boundary, and concurrent transitions, including guard conditions and data consistency checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad state-change triggers can activate the skill during unrelated discussions.

Mitigation: Confirm the user needs state-transition test design before applying its guidance.

Risk: Example state changes could be mistaken for permission to modify a real system.

Mitigation: Treat proposed transitions as test scenarios; require separate authorization before changing a system under test.

## Reference(s):

- [QA State Transition on ClawHub](https://clawhub.ai/kokxi/skills/qa-state-transition)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown tables, state-transition diagram, and test scenarios]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transition IDs and scenario links; nine-column test-case table; coverage statements scoped to the supplied requirements.]

## Skill Version(s):

1.7.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
