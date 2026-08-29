## Description:

Identifies common crop pests from crop leaf, bud, or fruit images and videos by calling server-side APIs and returning pest types with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting agricultural workflows use this skill to analyze crop media for early pest identification and structured reporting. The skill is intended to report observed pest types, counts, confidence, and report links rather than provide pesticide or treatment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop media or URLs are sent to configured backend services for analysis.

Mitigation: Review the configured endpoints and data retention policy before use, and avoid submitting media that contains unrelated sensitive information.

Risk: The skill can create a local workspace identity and SQLite database and store tokens or profile data for later requests.

Mitigation: Install only in a trusted workspace, restrict access to workspace data files, and clear or rotate stored identity data when it is no longer needed.

Risk: History queries retrieve cloud report records associated with the active identity.

Mitigation: Confirm the intended identity context before using history-list commands and review backend access controls for report history.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a requested file path; history queries return cloud report records as structured text.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
