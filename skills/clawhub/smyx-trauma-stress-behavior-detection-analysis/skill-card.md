## Description:

Analyzes fixed-camera emergency shelter video to flag acute stress behavior patterns such as stupor, tremor, unresponsiveness, and hypervigilance for authorized psychological rescue review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency-response developers and authorized shelter operations teams use this skill to analyze shelter or temporary-resettlement camera footage, produce behavior-observation alerts, and guide human review by qualified psychological rescue staff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive shelter footage and crisis reports are sent to cloud services.

Mitigation: Install only in an authorized emergency-response setting, and confirm consent or legal authority, tenant scoping, retention limits, and face blurring before processing real footage.

Risk: Identity or token data may be silently created, reused, or stored.

Mitigation: Review credential handling and storage, restrict access to authorized operators, and verify secure storage before deployment.

Risk: Configured endpoints may include development or private HTTP URLs.

Mitigation: Review and approve all configured service endpoints before installation or live operation.

Risk: Behavior-observation alerts could be mistaken for clinical diagnoses or automatic dispatch decisions.

Mitigation: Require human review by qualified psychological rescue staff and present outputs as visual behavior observations, not ASD/PTSD diagnoses or medication guidance.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON-formatted structured analysis reports, with optional saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior-observation alerts, crisis levels, location hints, PFA guidance, report links, and history-list results.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter and release changelog mention 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
