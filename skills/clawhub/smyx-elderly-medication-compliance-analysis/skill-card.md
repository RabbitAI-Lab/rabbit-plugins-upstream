## Description:

Analyzes medication-area video to identify pick-up, hand-to-mouth, and swallowing actions and report observed medication adherence steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and care staff can use this skill to review medication-time videos and see whether pick-up, hand-to-mouth, and swallowing actions were observed. It can also retrieve prior adherence reports for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private medication videos may be uploaded despite a no-analysis option, and the selected server address may be ignored.

Mitigation: Wait until the no-analysis and server-selection issues are fixed before using private footage. Confirm provider retention, deletion, account, and token-handling policies; obtain informed consent for remote processing; and verify monitoring and caregiver alerts independently.

## Reference(s):

- [Medication analysis API reference](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured medication-step results and adherence status; report lists can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected steps, confidence, event details, alerts, snapshots, and report links; does not provide medical advice.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
