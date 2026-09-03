## Description:

Transform a described human/business process into an executable automation design by separating deterministic steps, agentic reasoning, existing systems, and human gates; define triggers, data, decisions, exceptions, controls, and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and process owners use this skill to convert rough SOPs, workflows, forms, emails, spreadsheets, or diagrams into executable automation designs with clear implementation modes, interfaces, controls, and completion evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated automation plans may affect money, accounts, customer data, or production workflows if implemented without review.

Mitigation: Review generated plans before implementation, especially permissions, side effects, human approvals, rollback, and completion evidence.

Risk: Ambiguous business policy or unresolved exceptions could be automated as if they were known rules.

Mitigation: Keep explicit human or knowledge-resolution gates for unclear policy, missing data, or risk outside the accepted automation boundary.

## Reference(s):

- [Implementation Modes](references/implementation-modes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown with structured tables and optional Mermaid or BPMN-like pseudocode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an execution table, decision rules, exceptions, systems and permissions, observability, completion criteria, and a rollout or dry-run plan.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
