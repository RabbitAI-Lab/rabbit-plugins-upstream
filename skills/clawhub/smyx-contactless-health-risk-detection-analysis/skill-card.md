## Description:

Combines frontal facial image capture with multimodal physiological feature analysis to provide early risk screening and alerts for chronic and acute conditions such as heart attack, stroke, hypertension, and hyperlipidemia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to submit frontal face images, videos, or media URLs for cloud-based early health-risk screening and to retrieve structured historical screening reports. Results are screening support only and do not replace professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face images, videos, or provided media URLs to a remote service and handles biometric and health-related data.

Mitigation: Use only with clear user consent, approved data-handling terms, and environments where cloud processing of face and health data is permitted.

Risk: The skill creates or reuses an internal identity and stores authentication tokens locally.

Mitigation: Review local token storage, access controls, and cleanup practices before installing or running the skill in shared or regulated environments.

Risk: Screening outputs may be mistaken for medical diagnosis.

Mitigation: Present results as preliminary screening support and direct users to professional medical evaluation for high-risk or concerning findings.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files]

**Output Format:** [Markdown and JSON structured reports, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud report history and export report links; uploaded or URL-based media is processed by a remote health screening service.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
