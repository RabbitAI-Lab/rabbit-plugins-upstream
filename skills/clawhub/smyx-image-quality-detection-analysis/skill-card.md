## Description:

Detects quality issues in camera footage such as black or white screens, color cast, stripes, noise, and blurriness for security surveillance and camera self-check workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and developers use this skill to analyze camera images, video frames, or public media URLs for common image-quality failures and to retrieve cloud-hosted historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analyzed media and submitted URLs are sent to lifeemergence.com cloud services for processing.

Mitigation: Use only media and URLs whose cloud processing and retention model is acceptable; avoid private, internal, or sensitive surveillance footage.

Risk: The skill silently creates or reuses a local identity, provisions a remote-service account, and stores service tokens in the workspace data database.

Mitigation: Install only in workspaces where local token storage and remote account provisioning are acceptable; review or clear workspace data before sharing the environment.

Risk: Historical report lookup retrieves cloud-hosted records associated with the resolved local identity.

Mitigation: Run history queries only from authorized identities and avoid exposing generated report links beyond the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API error-code reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, analysis, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, quality findings, recommendations, report records, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image or video files and network media URLs; configured limit is 10 MB and documented formats include jpg, jpeg, png, mp4, avi, and mov.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
