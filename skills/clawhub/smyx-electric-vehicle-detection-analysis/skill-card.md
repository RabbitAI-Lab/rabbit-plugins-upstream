## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas from videos, images, or media URLs, then returns violation counts, alert levels, and management suggestions for safety teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External safety, facilities, and operations teams use this skill to analyze surveillance media for electric motorcycles or e-bikes in restricted areas. It supports park, community, campus, parking-lot, roadway, and similar safety-management workflows where reports should be reviewed by a human before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, or media URLs are sent to the Life Emergence/Open Life Emergence backend for analysis.

Mitigation: Use only media approved for that backend, and review the service's handling of uploaded media and report retention before processing sensitive footage.

Risk: Reports are tied to an automatically managed local identity, and authentication tokens may be stored locally.

Mitigation: Review account creation, local token storage, and report-history behavior before installation; restrict local file access and rotate or remove stored tokens when no longer needed.

Risk: Computer-vision reports may incorrectly classify vehicles or violation severity.

Mitigation: Treat reports as safety-management aids and require human review before enforcement, cleanup, or other operational action.

## Reference(s):

- [Electric Vehicle Detection Analysis API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis reports with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include violation counts, risk scores, alert levels, management warnings, suggestions, report links, and history-list results.]

## Skill Version(s):

9.9.15 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
