## Description:

Part of the Overpowered skill suite. Transform a described human/business process into an executable automation design by separating deterministic steps, agentic reasoning, existing systems, and human gates; define triggers, data, decisions, exceptions, controls, and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and process owners use this skill to turn rough business-process descriptions, SOPs, workflow artifacts, and examples into executable automation designs. It helps classify each step by the simplest reliable implementation mode and define interfaces, exceptions, controls, observability, and completion evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide sensitive workflow details, business documents, screenshots, forms, emails, or spreadsheets while using the skill.

Mitigation: Review inputs before use and redact confidential, regulated, or unnecessary data from process materials.

Risk: Generated automation designs may propose system permissions, side effects, or human approval gates that are incomplete or inappropriate for the business context.

Mitigation: Review the design before implementation and require dry runs or explicit approvals for workflows with side effects, scale, or authority concerns.

## Reference(s):

- [Implementation Modes](references/implementation-modes.md)
- [Overpowered Skill Suite](https://github.com/raguets/overpowered)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown process design with a step table and optional Mermaid or BPMN-like pseudocode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes implementation modes, interfaces, exception and failure behavior, controls, observability, completion criteria, and rollout or dry-run guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
