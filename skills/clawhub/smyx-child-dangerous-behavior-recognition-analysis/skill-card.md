## Description:

Analyzes videos for hazardous child behaviors such as climbing, playing with fire, touching electrical sources, and risky actions near windows, and provides alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and staff in homes, nurseries, and classrooms can analyze monitoring videos for potentially hazardous child behavior and review alerts or historical reports. Alerts should be checked by a person rather than treated as a substitute for supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's videos or video URLs may be sent to external analysis services.

Mitigation: Obtain appropriate consent and review the external data flow before submitting footage from homes, nurseries, or classrooms.

Risk: The skill may silently associate analysis with an identity and store account tokens locally.

Mitigation: Review identity and local token storage practices before installation; restrict access to the workspace and stored credentials.

Risk: Historical cloud reports may be retrieved automatically.

Mitigation: Limit use to authorized operators and review who can access historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report list with links; optional JSON output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk alerts, suggested actions, and report links when available.]

## Skill Version(s):

1.0.16 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
