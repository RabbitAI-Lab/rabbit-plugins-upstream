## Description:

Analyzes local OpenClaw usage logs to estimate token costs, project spending, check budgets, and suggest cheaper model routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chris](https://clawhub.ai/user/chris)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to understand model-by-model token spending, monitor a budget, and estimate savings from switching models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local usage logs, including auto-detected paths.

Mitigation: Confirm the selected file is an intended OpenClaw usage log before analysis.

Risk: Default prices and monthly projections may not match actual bills.

Mitigation: Use current pricing overrides and present projections as estimates.

Risk: Recurring budget checks may create unwanted monitoring or alerts.

Mitigation: Set up scheduled checks only when the user requests them.

## Reference(s):

- [Token Cockpit on ClawHub](https://clawhub.ai/chris/skills/skill-doctor)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Plain text or JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spend estimates, monthly projections, budget alerts, and model-switching savings suggestions.]

## Skill Version(s):

1.1.0 (source: ClawHub release; bundled skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
