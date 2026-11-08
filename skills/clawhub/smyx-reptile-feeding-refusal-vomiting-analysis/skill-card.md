## Description:

Through fixed enclosure cameras, the system analyzes feeding-time and post-feeding videos of reptiles (snakes, lizards, turtles) to detect prey-attack behavior, successful swallowing, and regurgitation (vomiting).

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and breeding-facility operators use the skill to review feeding videos, record prey attacks, swallowing, refusal, or regurgitation, and receive event summaries and alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential forwarding, account registration, and user-data handling need clarification.

Mitigation: Avoid installation or account linking until credential scope, registration behavior, collected data, and access are clearly documented and reviewed.

Risk: The remote video-processing disclosure is unclear.

Mitigation: Do not submit enclosure video until the processing destination, retention, and sharing practices are explained; submit only footage you are comfortable sending for remote analysis.

Risk: Some reported user-management and export behavior may not align with the described reptile-video analysis purpose.

Mitigation: Review requested actions and data flows before use, and limit access to the accounts and information needed for the task.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports and Markdown historical-report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include event labels, confidence values, alert levels, recommended actions, and report links; results describe observed behavior and are not a veterinary diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
