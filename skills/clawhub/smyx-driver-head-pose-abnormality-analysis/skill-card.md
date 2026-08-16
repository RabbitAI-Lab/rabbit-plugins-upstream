## Description:

Analyzes in-cabin DMS camera images or videos for driver head pitch and yaw to identify sustained head-down or side-view distraction events and return structured alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet-safety teams use this skill to analyze driver-facing DMS camera media for head-pose abnormalities, distraction events, warning classifications, and report links. It supports passenger cars, commercial vehicles, ride-hailing fleets, and freight fleet monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing video may contain sensitive biometric or workplace-monitoring data and is uploaded or sent by URL to a configured remote service.

Mitigation: Use only with explicit driver or employee consent, approved data-processing terms, controlled workspaces, and retention rules for uploaded media and generated reports.

Risk: The skill can silently create or reuse a local identity and store service tokens in workspace data.

Mitigation: Limit workspace access, review local data locations before deployment, and delete local database or token data when the skill is no longer needed.

Risk: Historical report queries can retrieve account-linked driving analysis records.

Mitigation: Restrict use to authorized operators and verify that report access aligns with internal privacy and fleet-monitoring policies.

Risk: Head-pose estimates can be less reliable when the driver's face or head contour is unclear, such as with hats, masks, sunglasses, glare, vibration, low frame rate, or low resolution.

Mitigation: Require suitable DMS camera placement, at least 25 FPS and 480p input, stable face visibility, and human review before treating alerts as operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON text with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured detection results, warning messages, recommended actions, report export links, and historical report lists.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
