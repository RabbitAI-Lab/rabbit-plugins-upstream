## Description:

Using an in-cabin DMS camera, the system analyzes the driver's head pose in real time, computing head pitch (down/up) and yaw (left/right turn). When sustained head-down or side-view behavior exceeds configured thresholds, it produces a distracted-driving alert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet operators use the skill to analyze in-cabin driver video for sustained head-down or side-view behavior and produce distraction alerts and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags a mismatch between advertised real-time monitoring and video-report processing, undeclared account handling, and possible transfer or storage of footage, identity data, or tokens.

Mitigation: Review the security assessment and behavior before enabling; use authorized footage with driver consent, restrict credentials, and verify remote data handling and account actions.

Risk: Driver face video contains sensitive biometric information, and poor visibility can reduce head-pose estimate reliability.

Mitigation: Obtain driver consent, follow applicable privacy requirements, protect recordings, and treat alerts as an aid rather than a substitute for driver attention.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [API interface notes](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON analysis reports and Markdown summaries or report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include head-pose angles, distraction events, alert types, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
