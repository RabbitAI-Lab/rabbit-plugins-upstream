## Description:

Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, and provides structured data for precision agriculture decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers, agronomy teams, and developers use this skill to analyze plant images, videos, or public media URLs, classify growth stages, and produce structured reports with monitoring results, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs may be sent to the LifeEmergence cloud service and associated with an automatically managed identity.

Mitigation: Use only media and URLs suitable for external processing, avoid sensitive media and internal/private URLs, and confirm users accept cloud processing before installation.

Risk: The skill may create or reuse a cloud-linked identity and store authentication data locally.

Mitigation: Review the workspace data directory for the local SQLite user/token store after use and remove local credentials according to the deployment environment's retention policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return historical report lists and report links; analysis depends on user-provided plant media or public media URLs.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter and auto changelog mention 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
