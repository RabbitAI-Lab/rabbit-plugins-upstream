## Description:

Analyzes facial photos or videos for nine traditional Chinese medicine constitution types and provides wellness recommendations and access to historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and wellness practitioners use this skill to request a face-based TCM constitution assessment, receive lifestyle suggestions, or view previous assessment reports. Its results are for wellness reference, not a substitute for professional diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media and derived health assessments are sent to external lifeemergence.com services.

Mitigation: Obtain informed consent before submitting personal media and use the service only when its data-handling terms are acceptable.

Risk: The skill may automatically create or reuse an account and store identity or token data locally.

Mitigation: Review account creation and local credential handling before use; protect the local environment and restrict access to saved identity data.

Risk: History-related phrases can automatically retrieve account-linked reports from the cloud.

Mitigation: Confirm the intended account and the user's authorization before requesting or sharing historical reports.

Risk: Face-based constitution assessments and wellness suggestions may be mistaken for medical diagnoses.

Mitigation: Present results as wellness guidance only and refer medical concerns to a qualified clinician.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown or structured text/JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Constitution types, scores, wellness suggestions, and optional historical report lists.]

## Skill Version(s):

1.0.14 (source: server release metadata; bundled frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
