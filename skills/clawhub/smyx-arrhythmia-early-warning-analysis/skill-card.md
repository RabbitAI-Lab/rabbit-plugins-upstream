## Description:

Analyzes facial video for possible irregular heart rhythms and provides early cardiac-risk screening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and health-support agents use facial video to screen for possible premature beats, atrial fibrillation, tachycardia, and bradycardia, or to retrieve prior screening reports. Results are preliminary and do not replace an ECG or a clinician's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video and health information may be processed by a remote service and retained in cloud reports.

Mitigation: Obtain informed consent before submission and confirm that cloud processing and retention meet privacy requirements.

Risk: The skill silently creates or reuses a cloud-linked identity and stores authentication tokens in the workspace.

Mitigation: Disclose account linkage before use, restrict access to workspace data, and remove stored tokens when no longer needed.

Risk: An early warning could be mistaken for a medical diagnosis.

Mitigation: Treat findings as preliminary screening and seek ECG testing and clinical evaluation for concerning results.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured screening report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk indicators, recommendations, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
