## Description:

This skill analyzes UAV multispectral or high-resolution RGB farm imagery to compute vegetation indices and produce health-index heatmaps with abnormal-zone coordinates, area estimates, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External agricultural operators, drone service teams, and precision-agriculture developers use this skill to submit UAV imagery or imagery URLs and receive crop-health index summaries, heatmap links, abnormal-zone coordinates, and historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UAV imagery, report queries, and identity-linked requests may be sent to a configured external service.

Mitigation: Use only with data approved for that service, confirm endpoint scope before deployment, and avoid sensitive farm, geospatial, or business data unless the data owner has consented.

Risk: The skill may silently create or reuse local user identities and store account tokens in a workspace database.

Mitigation: Require an explicit login or consent flow, review local token storage controls, and clear generated local identities when no longer needed.

Risk: Health-index outputs may be mistaken for operational agronomy instructions.

Mitigation: Treat results as index-based screening and require field verification before farm operations or business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [API reference](artifact/references/api_doc.md)
- [Analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, health-index report links, abnormal-zone data, and optional historical report tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local files or pass remote imagery URLs to an external analysis service; supports optional result-file output.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
