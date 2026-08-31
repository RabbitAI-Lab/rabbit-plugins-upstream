## Description:

Generates state-transition test designs for valid, invalid, boundary, and concurrent state-machine flows, including triggers, preconditions, postconditions, and verification points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test designers use this skill to turn scenario trees and requirement analysis into state-transition coverage for business objects with multiple lifecycle states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad state-testing language and produce test designs that are not tailored enough for a specific system.

Mitigation: Confirm that the request is about state-transition testing and review generated cases against the actual requirements before use.

Risk: Examples involving payments, refunds, or account states could be mistaken for instructions to change real system state.

Mitigation: Treat generated content as test-design guidance only and do not apply examples to production systems without human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-state-transition)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test-case tables, state-transition lists, state diagrams, and scenario guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include traceability IDs, priority distribution guidance, coverage caveats, valid transitions, invalid transitions, and state-transition test scenarios.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
