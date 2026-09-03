## Description:

Based on computer vision, this skill analyzes respiratory videos or URLs to detect coughing, phlegm, and wheezing frequency, count episodes, and produce early health anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit respiratory health videos or video URLs for symptom frequency analysis, structured monitoring reports, health risk warnings, and report history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Respiratory health videos or URLs may be sent to the configured SMYX/Life Emergence remote service.

Mitigation: Use the skill only with explicit consent and appropriate privacy controls, and avoid patient or regulated health data unless those controls are in place.

Risk: The skill may create or reuse persistent local identity records and tokens for report history.

Mitigation: Review local identity handling before installation and use report-history features only where persistent identity records are acceptable.

Risk: Analysis results are health-monitoring guidance and are not a medical diagnosis.

Mitigation: Treat reports as supplementary monitoring information and direct users to professional medical care for diagnosis, severe symptoms, or clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Respiratory Symptom Recognition API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and optional JSON analysis output with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory symptom counts, risk level, health warnings, medical suggestions, report links, and report-history tables.]

## Skill Version(s):

1.0.15 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
