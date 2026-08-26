## Description:

Analyzes pet drying box video files or URLs through a backend API to detect early heat-stress signals such as panting intensity, tongue color, and movement frequency, then returns risk levels and intervention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, grooming stores, pet hospitals, and developers use this skill to review drying-box media for heat-stress warning signs and produce structured safety guidance. Results are for drying safety support and should not be treated as medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to a configured backend service for analysis.

Mitigation: Use only media the user is authorized to upload, disclose backend processing, and require explicit confirmation before upload.

Risk: The skill can silently create or reuse account identities and store service tokens in a local SQLite database.

Mitigation: Run in an isolated workspace, review local storage before reuse, and avoid sharing the workspace across unrelated users.

Risk: Cloud history report lookup may retrieve prior reports with limited user control.

Mitigation: Require explicit confirmation before history queries and show only report information appropriate for the current user context.

## Reference(s):

- [Pet Drying Box Heat Stress API Documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports, with optional Markdown tables for history reports and links to generated reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, optional pet type, detail level, output file path, and cloud history report listing.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
