## Description:

Analyzes pet image or video inputs through provider APIs to produce a 3D body-shape assessment, BCS 1-9 score, weight-category classification, structured observation report, history list, and report link without veterinary diagnosis or treatment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit multi-angle pet videos, video URLs, or images for body condition scoring and weight-management observation workflows. The skill can also retrieve cloud-hosted historical analysis reports associated with the current identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet videos, images, or media URLs may be sent to the provider's server for analysis.

Mitigation: Use only with approved media or URLs and confirm the provider endpoint and privacy expectations before submitting analysis requests.

Risk: The skill can silently link and persist local identity tokens or records.

Mitigation: Review identity and token storage, retention, and access controls before deployment.

Risk: Default configuration may include plaintext development API endpoints.

Mitigation: Confirm production HTTPS API configuration before installation or execution.

Risk: Cloud history retrieval may expose reports associated with the current identity.

Mitigation: Require explicit confirmation before retrieving historical reports.

## Reference(s):

- [ClawHub Skill Release Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Health Analysis API Reference](artifact/references/api_doc.md)
- [SMYX Analysis API Reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated report text to a local output file when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
