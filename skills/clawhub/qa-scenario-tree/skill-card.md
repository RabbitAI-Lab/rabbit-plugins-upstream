## Description:

This skill helps QA practitioners turn decomposed requirements into structured scenario trees covering happy paths, alternative paths, exception paths, business rules, and data flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and product teams use this skill after requirements decomposition to design traceable test scenarios for complex business workflows, page transitions, state changes, and exception handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may include real customer, payment, identity, financial, or production data while asking for QA scenarios.

Mitigation: Mask or remove sensitive data before using the skill, especially customer information, payment details, identity numbers, screenshots, and production records.

Risk: The skill is tailored for Chinese QA workflows and may trigger on broad test-scenario requests.

Mitigation: Confirm that the requested workflow and language fit the task before relying on the generated scenario tree.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-scenario-tree)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown scenario trees and test case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario outputs include unique scenario or test case IDs, linked requirement IDs, path type, priority, expected results, and risk level when supported by the input.]

## Skill Version(s):

1.7.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
