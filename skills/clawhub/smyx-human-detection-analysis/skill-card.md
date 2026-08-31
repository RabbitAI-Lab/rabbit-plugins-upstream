## Description:

Automatically detects personnel in target areas based on computer vision, supports real-time video stream detection, and produces structured monitoring reports for parks, offices, and restricted areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users can use this skill to submit surveillance video files or URLs for regional person detection, person counts, intrusion signals, and structured report output. It can also query previously generated cloud reports associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance media or media URLs are sent to a Life Emergence remote service for analysis.

Mitigation: Use only footage approved for that service, avoid sensitive or regulated environments until retention and handling terms are documented, and review the remote endpoint configuration before deployment.

Risk: The skill silently manages cloud identity and can store generated user identity, tokens, and profile fields in a local workspace database.

Mitigation: Run the skill in an isolated workspace, protect or rotate stored tokens, and clear the workspace data store when the deployment or user context changes.

Risk: Historical report queries retrieve cloud report history associated with the resolved user identity.

Mitigation: Limit access to agents and users authorized to view that report history, and confirm the expected identity before using report-listing workflows.

Risk: Bundled API reference material contains mismatched pet-health endpoints instead of only human-detection API documentation.

Mitigation: Validate operational endpoints against the scripts and publisher documentation before relying on the reference docs for integration or incident review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Common analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown status text with structured JSON analysis results and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; accepts mp4, avi, and mov inputs up to 10 MB.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
