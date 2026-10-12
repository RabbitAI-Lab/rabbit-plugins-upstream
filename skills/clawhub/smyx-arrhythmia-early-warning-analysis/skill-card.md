## Description:

Analyzes facial video for possible abnormal heart rhythms and provides an early-warning risk report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and health-focused application developers use facial video to screen for possible irregular heart rhythms and review prior warning reports. Results are early-warning information, not a substitute for ECG testing or clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video and inferred heart-health data are sent to a cloud service.

Mitigation: Obtain informed consent and confirm the service's privacy handling before submitting video.

Risk: The skill creates or reuses an internal identity and stores account and authentication tokens locally.

Mitigation: Restrict access to the workspace and avoid running it on shared or untrusted machines.

Risk: History requests can query sensitive cloud health reports automatically.

Mitigation: Require user confirmation before requesting report history.

Risk: A local import-hijacking flaw could run unintended code.

Mitigation: Use a trusted, isolated environment and prefer a release that fixes import precedence.

Risk: Screening results may be mistaken for a medical diagnosis.

Mitigation: Treat findings as preliminary and seek professional ECG testing and clinical assessment for concerning results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Analysis API documentation](artifact/references/api_doc.md)
- [Analysis API error codes](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export link or an optional saved result file.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
