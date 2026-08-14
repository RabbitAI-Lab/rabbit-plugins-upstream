## Description:

Analyzes UAV farm imagery to compute vegetation-index health maps, identify low-health zones, and return structured crop-vigor findings, statistics, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, agricultural analysts, farm operators, UAV service providers, and developers use this skill to submit UAV orthomosaic, multispectral, RGB, image, video, or URL inputs for vegetation-index analysis and historical report retrieval. It supports crop-health heatmaps, abnormal-zone coordinates and area estimates, coverage statistics, and report links for precision-agriculture review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm imagery, media URLs, and related account metadata may be sent to lifeemergence.com services for cloud analysis.

Mitigation: Use the skill only after confirming that the remote service, retention practices, and account handling are acceptable for the imagery being processed.

Risk: The skill can create or reuse an internal identity and store session tokens in the workspace data database.

Mitigation: Run it in an appropriate workspace, restrict access to workspace data, and clear or isolate the data directory when switching users or handling sensitive projects.

Risk: Sensitive geotagged farm imagery could expose operational or location information.

Mitigation: Avoid sensitive geotagged inputs unless their transfer and storage have been approved for the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured text with analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health-index map URLs, mean vegetation-index values, low-health zone coordinates and area estimates, crop coverage ratios, field health statistics, and historical report lists.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
