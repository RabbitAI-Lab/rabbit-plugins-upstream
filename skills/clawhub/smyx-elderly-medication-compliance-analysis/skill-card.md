## Description:

Analyzes medication-area images or videos for visible pick-up, hand-to-mouth, and swallowing steps, then returns a medication-adherence result and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and care staff can submit medication-area media to review whether the visible pick-up, hand-to-mouth, and swallow steps were observed, and retrieve prior analysis reports. The result is an auxiliary adherence check and does not provide medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Medication videos and report history contain sensitive health information and may be processed through a cloud service; account and data handling require care.

Mitigation: Obtain informed consent, review the service's data handling before uploading, and limit uploads and retention to what is needed.

Risk: The security assessment flags a mismatch between the described monitoring and the supplied-video workflow, so the observed result may not establish whether medication was taken.

Mitigation: Treat the result as an auxiliary check and have a caregiver confirm missed, uncertain, or consequential results before acting.

Risk: The security guidance flags unexpected account-registration behavior and cloud analysis.

Mitigation: Confirm which account is associated with an upload and its reports, and avoid uploading sensitive media until that association is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured adherence results and report data presented as text or JSON, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed medication steps, adherence status, confidence, alerts, and links to analysis reports.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
