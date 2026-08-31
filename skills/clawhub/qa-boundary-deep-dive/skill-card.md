## Description:

QA Boundary Deep Dive helps testers and developers identify boundary conditions across input, state, time, and resource dimensions, assign risk levels, and define expected results for test cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test designers use this skill to expand scenario trees and requirements into boundary-focused test cases for systems with input fields, state transitions, timing constraints, or resource limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or workspace inputs may include sensitive production data such as payments, identity information, screenshots, phone numbers, or customer records.

Mitigation: Use sanitized requirements and masked test data before invoking the skill.

Risk: Boundary-test guidance can be incomplete or misaligned when the supplied requirements or scenario tree are incomplete.

Mitigation: Review generated boundary cases against current requirements and mark uncovered modules with the reason they were not covered.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-boundary-deep-dive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown test case tables and structured boundary analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes boundary IDs, scenario traceability, risk levels, expected results, and coverage notes.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
