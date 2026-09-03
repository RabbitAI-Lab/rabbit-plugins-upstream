## Description:

Analyzes pet drying-box video files or URLs through Life Emergence cloud APIs to detect early heat-stress signals such as open-mouth panting intensity, tongue color, and body movement frequency, then returns risk levels, intervention suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, and agent developers use this skill to submit drying-box video evidence for cloud-based heat-stress warning analysis and to retrieve prior analysis reports. The output is intended as drying-safety support, not veterinary diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet drying-box videos or public video URLs are sent to the configured Life Emergence cloud service for analysis.

Mitigation: Use only when the user is comfortable sharing that media with the configured service, and avoid submitting unrelated, sensitive, or excessive footage.

Risk: The skill can create or reuse a local account identity and store tokens in a workspace SQLite database.

Mitigation: Prefer a single-user workspace, restrict local workspace access, and remove the local data database or rotate tokens when uninstalling or changing identities.

Risk: Historical report lookup is account-scoped and may expose prior analysis records in shared workspaces.

Mitigation: Use separate workspaces for separate users or roles, and review report history access before deployment in multi-user environments.

## Reference(s):

- [Pet Drying Box Heat Stress API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links; optional file output when an output path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts mp4, avi, or mov inputs up to 10 MB; can analyze local files or public video URLs and can list account-scoped historical reports.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
