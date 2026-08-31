## Description:

Use when the user asks what car maintenance is due or overdue, whether a service can wait, what a dealer 'recommended service' actually contains, or to build a maintenance schedule and budget from mileage, vehicle age, and service history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and vehicle owners use this skill to evaluate due or overdue maintenance, compare dealer recommendations against a generic schedule, and plan a 24-month maintenance budget from odometer, vehicle age, driving profile, and service history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance outputs are generic estimates and may not match a specific vehicle, warranty requirement, or local inspection rule.

Mitigation: Verify intervals and required inspections against the vehicle owner's manual, service records, and applicable local rules before acting.

Risk: Service-history text can contain unnecessary personal or location details.

Mitigation: Enter only the task, odometer, and service date needed for the calculation.

Risk: The tool schedules maintenance but does not diagnose symptoms such as noises, leaks, warning lights, or brake issues.

Mitigation: Use a qualified mechanic for symptoms, safety concerns, and model-specific repair decisions.

## Reference(s):

- [Maintenance Model](references/maintenance-model.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/car-maintenance-timeline)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide local Python command examples and advisory maintenance summaries; no network access is required by the artifact.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
