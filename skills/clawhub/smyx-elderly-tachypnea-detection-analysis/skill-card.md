## Description:

Using a fixed bedroom camera, this skill analyzes an elderly person at rest to estimate respiratory rate and flag possible tachypnea or dyspnea without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care operators use this skill to analyze fixed-camera bedroom video or image inputs for resting respiratory-rate signals, structured risk levels, report links, and historical respiratory-monitoring reports. It is an assistive monitoring skill and should not be treated as a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom video or images may be sent to a remote analysis service.

Mitigation: Use the skill only with informed consent from the monitored person or authorized caregiver, and confirm the configured service endpoint is trusted before submitting media.

Risk: Cloud health-report history can be retrieved for the resolved identity.

Mitigation: Run history queries only in workspaces where identity reuse is acceptable, and review access controls before sharing outputs or report links.

Risk: The skill may silently create or reuse an identity and store authentication tokens locally.

Mitigation: Inspect local credential storage and workspace sharing practices before installation, especially on shared machines or multi-user agent environments.

Risk: Respiratory alerts can be mistaken for medical diagnosis.

Mitigation: Present results as assistive monitoring only, require human review for urgent alerts, and escalate to appropriate medical care when symptoms or risk levels warrant it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON respiratory-analysis report with shell command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory rate, breathing-pattern assessment, signal quality, risk level, alert text, medical follow-up hint, and historical report tables.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
