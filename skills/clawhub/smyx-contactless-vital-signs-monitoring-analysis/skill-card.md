## Description:

Analyzes camera video for heart rate, respiration, blood oxygen, and heart rate variability without a wearable device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use the skill to request non-contact vital-sign analysis of face videos and view structured results or past reports. Results are for health reference, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face videos or video URLs are sent to external cloud services for analysis.

Mitigation: Obtain informed consent and avoid submitting sensitive footage unless the cloud service's privacy terms are acceptable.

Risk: The skill silently creates or reuses a local identity and retains account tokens for later report lookups.

Mitigation: Use a separate workspace for sensitive testing, avoid shared machines, and review or delete stored workspace data when access is no longer needed.

Risk: Vital-sign estimates could be mistaken for clinical measurements or a diagnosis.

Mitigation: Treat results as health reference only; consult a clinician and use appropriate medical measurement for clinical decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown table of historical reports; JSON is available for detailed results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include risk notes, recommendations, and report links.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
