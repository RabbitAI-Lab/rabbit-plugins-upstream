## Description:

Analyzes camera footage to estimate heart rate, respiration, blood oxygen, and heart rate variability without wearable devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to submit local or URL-based face video for non-contact vital-sign analysis and to retrieve prior cloud reports. Results are health-reference outputs and are not a substitute for professional medical measurement or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face video and inferred health data may be sent to the vendor's cloud service for analysis.

Mitigation: Obtain explicit user consent before analysis, disclose the remote service path, and avoid submitting sensitive recordings unless the user accepts that data handling.

Risk: The skill can silently create or reuse an account identity and persist account tokens locally.

Mitigation: Review local data and token storage before deployment, restrict filesystem access where possible, and prefer a release that makes identity creation and token persistence explicit.

Risk: Cloud history lookup can retrieve prior reports associated with the resolved identity.

Mitigation: Limit history queries to authorized users and make report-history retrieval a deliberate, consented action.

Risk: Vital-sign estimates may be interpreted as medical conclusions.

Mitigation: Present outputs as health-reference information only and direct users to professional medical measurement or clinical care for diagnosis or abnormal results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown and JSON report text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and history-list results returned by the vendor API.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
