## Description:

Provides reusable QA checklist templates for common feature types including forms, lists, carts, payments, imports and exports, approvals, notifications, and permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, testers, and developers use this skill to identify relevant heuristic test points and produce structured test-case guidance when evaluating common product features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad testing or checklist requests when a more specialized QA workflow is needed.

Mitigation: Use a specialized QA skill for deeper scenario generation, boundary analysis, or domain-specific testing.

Risk: Checklist examples may describe create, update, or delete operations against a tested product.

Mitigation: Treat these examples as test-design guidance and avoid executing destructive actions against production data.

## Reference(s):

- [Feature-Type Heuristic Checklist Reference](artifact/references/checklists.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-heuristic-checklist)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured test-case tables and checklist sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include heuristic checklist items, covered and uncovered areas, exploration guidance, and risk levels.]

## Skill Version(s):

1.7.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
