## Description:

Helps QA practitioners design state-machine tests for valid, invalid, boundary, and concurrent transitions while recording triggers, preconditions, postconditions, and verification points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test designers use this skill to convert stateful business workflows into state-transition test cases, including legal transitions, illegal transitions, edge conditions, concurrency checks, and traceability IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad Chinese phrases about state changes.

Mitigation: Install it as a read-only QA test-design skill and confirm that state-transition analysis is appropriate for the request before applying its output.

Risk: Example business states could be mistaken for instructions to alter a live system.

Mitigation: Treat generated state transitions and test cases as design guidance only, and review them before using them with any production system.

Risk: Standalone use may omit context supplied by the broader QA skill bundle.

Mitigation: Use this release for state-transition test design, and review the separately recommended full QA bundle before installing or relying on the broader workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-state-transition)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown tables and structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces state-transition diagrams or lists, valid and invalid transition lists, test scenarios, and traceability IDs; the security evidence reports no credential access, persistence, or data exfiltration request.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
