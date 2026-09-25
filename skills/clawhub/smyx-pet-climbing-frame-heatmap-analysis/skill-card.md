## Description:

Analyzes cat tree video files or video URLs through a cloud API to report layer dwell time, jumps or transitions, activity density, and a 2D activity heatmap without providing medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate cat activity distribution on a climbing frame or cat tree from uploaded or URL-based video. It is intended for enrichment and activity monitoring workflows, not veterinary diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet or household video files and supplied video URLs to the lifeemergence cloud service for analysis.

Mitigation: Use only footage and URLs whose cloud processing is acceptable, and avoid sensitive household footage or private/internal URLs unless that data flow has been approved.

Risk: The skill can create or reuse an internal identity, store local tokens, and retrieve cloud report history with limited user control.

Mitigation: Deploy it only in environments where token storage, identity reuse, and report-history access are acceptable and can be governed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a file when requested; history queries are rendered as a Markdown table from cloud results.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
