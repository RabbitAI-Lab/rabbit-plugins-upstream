## Description:

Analyzes cat climbing frame or cat tree videos with remote APIs to produce activity metrics, dwell-time and jump or transition counts, and a 2D heatmap for exercise and enrichment review without disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze cat tree video footage or video URLs, review layer-level activity distribution, and retrieve cloud report history for pet behavior monitoring. The generated results are for exercise and enrichment observation, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload home pet videos or submit video URLs to a remote service.

Mitigation: Use only footage appropriate for remote processing and confirm the publisher's API destination, retention policy, and deletion process before installation.

Risk: The skill can create or reuse an internal identity and store authentication tokens in a local workspace database.

Mitigation: Run it only in a workspace where local identity and token storage is acceptable, and review or clear stored credentials after use.

Risk: The security guidance flags dev HTTP endpoints in a published package.

Mitigation: Do not use the package for production workflows until the publisher explains the endpoint configuration and provides appropriate production HTTPS endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown text with structured JSON-style analysis, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local video inputs are documented as mp4, avi, or mov up to 10 MB; URL inputs are submitted to the remote analysis API.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
