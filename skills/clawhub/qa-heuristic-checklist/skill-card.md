## Description:

Provides Chinese-language testing checklists for common feature types, including forms, shopping carts, payments, imports, approvals, notifications, and access control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers and developers use this skill to identify feature-specific test cases, edge cases, and gaps when designing tests for new functionality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist examples describing deletion or modification could be mistaken for instructions to change real test data.

Mitigation: Treat examples as test scenarios; use isolated test data and review any destructive test steps before execution.

Risk: Generic checklists may omit feature-specific risks or overstate test coverage.

Mitigation: Adapt the checklist to requirements and historical defects, document uncovered areas, and avoid claiming complete coverage.

## Reference(s):

- [Feature-type testing checklists](references/checklists.md)
- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-heuristic-checklist)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Chinese-language Markdown checklist and nine-column test-case table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes covered and uncovered areas and exploratory testing guidance.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
