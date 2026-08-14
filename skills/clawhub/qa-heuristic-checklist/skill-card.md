## Description:

Provides heuristic QA checklist templates for common feature types such as login, payment, search, shopping cart, import/export, approval workflows, notifications, and permission management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers, developers, and teams use this skill to identify relevant test areas for new or unfamiliar feature types and avoid missing common risk points. It helps structure exploratory testing and checklist-driven test planning across functional, security, compatibility, and performance concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist examples include deletion, payment, refund, and permission-testing scenarios that can affect real data if executed directly in production.

Mitigation: Use sandbox or test environments, test accounts, and normal change controls before applying destructive or payment-related scenarios.

Risk: A generic heuristic checklist may miss product-specific rules, regulatory constraints, or historical defect patterns.

Mitigation: Review the checklist against requirements, recent incidents, and domain-specific acceptance criteria before relying on it for release decisions.

## Reference(s):

- [Complete functional heuristic checklists](references/checklists.md)
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-heuristic-checklist)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown checklist with covered areas, uncovered areas, and exploratory testing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference heuristic identifiers and feature-type coverage notes]

## Skill Version(s):

1.6.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
