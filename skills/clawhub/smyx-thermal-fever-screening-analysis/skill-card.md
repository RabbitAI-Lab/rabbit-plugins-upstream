## Description:

Analyzes thermal video of groups to flag people whose skin-surface temperature differs from the group average and recommends thermometer rechecks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Households and staff overseeing small gatherings use thermal camera footage to identify relative skin-temperature anomalies and review historical screening reports. Alerts prompt a calibrated thermometer recheck rather than a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive thermal/video inputs and report history are sent to a cloud service.

Mitigation: Obtain participants' consent and confirm the provider's retention and deletion practices before use.

Risk: The skill can silently create or reuse an account and store persistent tokens locally.

Mitigation: Review the need for automatic identity creation and local token storage before installation.

Risk: Relative skin-temperature readings may mislead when affected by clothing, activity, or ambient heat.

Mitigation: Treat alerts as screening only; recheck with a calibrated thermometer and seek clinical assessment where appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)
- [Screening API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured screening results and Markdown report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes relative temperature alerts, recheck advice, and report links when available.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
