## Description:

FDE Delivery Router is a stateful control router for identifying the current stage of a customer engagement, selecting the appropriate FDE specialist skill, preserving delivery gates and project state, and identifying one next material action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, delivery leads, and FDE teams use this skill to classify an engagement, select the appropriate specialist FDE skill, preserve project-state decisions, and identify one accountable next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local project state files can capture engagement status, owners, decisions, and history.

Mitigation: Keep state files in the intended project directory and avoid storing secrets or raw customer material.

Risk: Advancing stages, skipping gates, or changing owners and decisions can affect delivery commitments.

Mitigation: Review state changes and require human confirmation before advancing stages, skipping quality gates, or modifying accountable decisions.

## Reference(s):

- [Routing Contract](references/routing-contract.md)
- [Project State Contract](references/project-state-contract.md)
- [Engagement State Machine](references/engagement-state-machine.md)
- [FDE Operating Model](references/fde-operating-model.md)
- [Router Quality Rubric](references/router-quality-rubric.md)
- [Router Field Handbook](references/router-field-handbook.md)
- [Input Examples](references/input-examples.md)
- [Public Method Sources](references/public-sources.md)
- [ClawHub Skill Page](https://clawhub.ai/xukun0821/skills/fde-delivery-router)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured routing decisions and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain local fde-project.json and append fde-events.jsonl when stateful delivery is authorized.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
