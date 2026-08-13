## Description:

Analyzes fixed-camera videos of an older person's resting hand to estimate tremor frequency, pixel amplitude, affected side, and a non-diagnostic resting-tremor risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, care-facility staff, and health-support developers use this skill to submit resting-hand videos or URLs for non-diagnostic tremor screening and to retrieve historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly hand videos and report metadata are sent to a configured cloud health-analysis service.

Mitigation: Use only with explicit consent from the recorded person or caregiver, and avoid submitting videos that are not needed for the stated screening task.

Risk: The skill can silently create or reuse an internal identity and associate report history with it.

Mitigation: Run the skill in a dedicated workspace for sensitive use and review account-linking behavior before deployment.

Risk: Reusable local account tokens may be stored and used for subsequent cloud requests.

Mitigation: Restrict workspace access, rotate or remove stored credentials when access is no longer needed, and review the skill before installing it in shared environments.

Risk: Resting-tremor outputs may be mistaken for a clinical diagnosis.

Mitigation: Present results as non-diagnostic screening signals and route concerning results to qualified medical review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON-style analysis results, risk labels, report links, and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video file paths or public video URLs; history queries return cloud-backed report lists.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
