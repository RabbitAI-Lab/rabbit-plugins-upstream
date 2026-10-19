## Description:

Analyzes medication-area video for medication pick-up, movement to mouth, and apparent swallowing, then returns a structured compliance report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and families use this skill to review an older person's medication-taking steps from video and check reports for potentially incomplete sessions. Visual results are aids to human follow-up, not medical advice or proof that a dose was swallowed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive medication-area video or video URLs are sent to a remote service.

Mitigation: Obtain informed consent from the monitored person or guardian and use a controlled media source and account.

Risk: The skill can silently create or reuse an identity and retain account tokens and report history locally.

Mitigation: Review local account storage and limit access to credentials and report history.

Risk: Video-based assessment may incorrectly mark a medication session incomplete or complete.

Mitigation: Have a caregiver confirm concerning results directly; do not use the report to change medication instructions.

## Reference(s):

- [Medication compliance API reference](references/api_doc.md)
- [Analysis API and error codes](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)

## Skill Output:

**Output Type(s):** [Text, Reports, Links]

**Output Format:** [Text with structured analysis results and report links; optional saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical reports; results require human confirmation.]

## Skill Version(s):

1.0.14 (source: ClawHub server release; bundled SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
