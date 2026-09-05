## Description:

Analyzes UAV farm imagery to compute vegetation indices such as NDVI and NDRE, generate a crop health-index heatmap, and identify low-health zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agricultural operators can use this skill to analyze UAV orthophotos, mosaics, image files, videos, or URLs for farm health-index reporting. It supports vegetation-index summaries, heatmap outputs, abnormal-zone coordinates and areas, and cloud history lookup for prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UAV imagery, farm/geospatial data, submitted URLs, and account-linked report history may be sent to configured backend services.

Mitigation: Install only after reviewing the configured backend destination, data retention behavior, and deletion options; avoid using sensitive farm imagery until those details are acceptable.

Risk: The skill can create or reuse local identity state and tokens without user-facing setup.

Mitigation: Run in an isolated agent environment, inspect local credential and token storage before reuse, and remove stored identity state when the skill is no longer needed.

Risk: Backend destinations and development or private endpoints are not fully documented in the public skill materials.

Mitigation: Require clear endpoint documentation and remove development or private endpoints before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [API 接口文档](artifact/references/api_doc.md)
- [SMYX analysis API docs](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report text and JSON-like structured analysis, optionally with report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return cloud-backed analysis results or account-linked history records; local file inputs are constrained by supported image/video formats and file size.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
