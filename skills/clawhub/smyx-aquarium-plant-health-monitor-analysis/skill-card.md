## Description:

Analyzes aquarium plant images or videos for visible health symptoms and returns an assessment with care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquascapers, and aquarium shops use the skill to assess submerged plants from images or videos, identify visible symptoms, and review general care directions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may not be honored, and automatic account setup may reuse or store credentials without sufficient user control.

Mitigation: Require a working no-analysis mode and clear controls for uploads, account registration, and credential storage before use.

Risk: Uploads and cloud use may involve sensitive footage, reusable credentials, and service costs.

Mitigation: Use non-sensitive footage and a dedicated service identity, check expected cloud costs, and do not provide a valuable API secret while it can be reused as an account identifier.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Analysis API reference and error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured health assessment, visible symptom findings, care suggestions, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessment and general care directions; no specific water chemistry parameter settings.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
