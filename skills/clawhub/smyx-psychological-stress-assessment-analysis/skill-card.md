## Description:

Analyzes facial images or video through a cloud service to estimate stress, anxiety, and depression tendencies and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can submit facial images or video for non-diagnostic stress assessment, review reported anxiety and depression tendencies, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media and inferred mental-health information are sent to cloud services.

Mitigation: Submit media only with clear consent, especially for other people or minors; confirm how uploads and reports are accessed, retained, and deleted.

Risk: Persistent identity and token records can be created or reused without an explicit prompt.

Mitigation: Confirm identity and token storage, access, and deletion practices with the publisher before installation.

Risk: Stress, anxiety, and depression assessments may be mistaken for diagnoses.

Mitigation: Use results only as non-diagnostic guidance and seek qualified professional help for persistent concerns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text with structured JSON results and report links; optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical reports; assessments are not clinical diagnoses.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; artifact frontmatter lists 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
