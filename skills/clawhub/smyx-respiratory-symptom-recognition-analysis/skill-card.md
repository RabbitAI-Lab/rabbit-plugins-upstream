## Description:

Detects coughing, expectoration, and wheezing in respiratory symptom videos, counts episodes, and produces early health-anomaly alerts and monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to submit respiratory monitoring videos or video URLs for symptom-count analysis, health risk warnings, care suggestions, report links, and cloud history report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive respiratory-health media may be uploaded to cloud APIs.

Mitigation: Review data handling, consent, retention, and endpoint authorization before installing or running the skill.

Risk: Security evidence reports weak transport controls and requires HTTPS-only production endpoints.

Mitigation: Use only reviewed HTTPS production endpoints and remove or block HTTP or local test endpoints from release artifacts.

Risk: The skill may silently create or reuse an identity and store reusable tokens locally.

Mitigation: Make identity scope explicit, protect or remove local token storage, and ensure prior reports are retrieved only for the intended user.

Risk: Respiratory symptom analysis can be mistaken for medical diagnosis.

Mitigation: Present results only as health-monitoring support and direct users to professional medical care for diagnosis or urgent symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Respiratory Symptom API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report or JSON payload with report links; shell command examples for execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes mp4, avi, and mov inputs up to 10 MB and can query cloud-stored history reports.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
