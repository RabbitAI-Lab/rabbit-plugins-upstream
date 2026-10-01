## Description:

Analyzes respiratory videos for coughing, expectoration, and wheezing episodes and provides symptom counts, health alerts, and monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, caregivers, and healthcare teams can review respiratory symptom counts, alerts, and historical monitoring reports from videos. Results support health monitoring and do not replace medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health videos or URLs are sent to a cloud analysis service, and historical reports can be queried.

Mitigation: Obtain user consent and confirm the publisher and data retention policy before sending health media or accessing reports.

Risk: The skill may silently create or reuse an identity and persist tokens or profile data in the workspace data directory.

Mitigation: Review the account model and restrict access to stored identity and token data before installation.

Risk: Symptom assessments and alerts may be mistaken for a clinical diagnosis.

Mitigation: Treat results as monitoring aids, not medical advice; seek professional assessment for concerning symptoms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Respiratory symptom analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or Markdown monitoring reports and historical report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom counts, health warnings, suggestions, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
