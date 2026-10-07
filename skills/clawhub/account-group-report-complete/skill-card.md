## Description:

Builds grouped account reports from a report request, saves a local report, and optionally delivers it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers use this skill to turn an account report request into a grouped report and, when configured, submit the report to a delivery destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive report data without a separate confirmation step.

Mitigation: Clear delivery settings for local-only runs; verify the destination and provide credentials only for trusted services before enabling delivery.

Risk: The workflow writes a report to the chosen output directory.

Mitigation: Use a dedicated output directory.

## Reference(s):

- [Account Report Recipe Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/account-group-report-complete)

## Skill Output:

**Output Type(s):** [JSON, CSV files]

**Output Format:** [JSON response with report and delivery receipts; local CSV report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [External delivery is optional; without delivery configuration, the report remains local.]

## Skill Version(s):

1.2.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
