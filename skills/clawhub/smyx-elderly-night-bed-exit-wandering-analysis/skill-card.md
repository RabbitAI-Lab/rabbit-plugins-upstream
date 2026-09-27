## Description:

Analyzes nighttime bedroom or hallway video to report older adults' bed exits, time out of bed, wandering, and threshold-based alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care-service teams use the skill to review nighttime bedroom or hallway footage for prolonged bed exits and wandering, and to consult alerts and historical reports. Alerts support human review, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private nighttime bedroom footage is processed by an external cloud service.

Mitigation: Obtain clear consent before submitting footage, and ask the publisher about retention, deletion, access controls, and audit practices before using real resident data.

Risk: The skill may silently create or reuse an identity and retain authentication tokens in the workspace.

Mitigation: Review identity and local token storage behavior before installing; use only in an environment where both are acceptable.

Risk: Automated behavior alerts may be mistaken for confirmed emergencies.

Mitigation: Have caregivers promptly verify suspected falls or absences and take appropriate action rather than relying on alerts as a diagnosis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis results and alerts; historical report lists in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and risk alerts; not a medical diagnosis.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
