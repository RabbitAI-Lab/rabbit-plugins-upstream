## Description:

Analyzes fixed-camera classroom images or video to estimate class engagement, emotion distribution, low-engagement seat coordinates, heatmaps, alerts, teacher suggestions, and historical report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, school administrators, and classroom technology operators can use this skill to analyze classroom footage for aggregate engagement trends, anonymous low-engagement seat positions, heatmaps, alerts, and teaching suggestions. It also supports querying cloud-hosted historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive classroom footage and report history may be processed through cloud services without enough disclosure.

Mitigation: Require clear cloud upload, retention, access, and deletion documentation before use, and obtain school administrator and parent consent for classroom footage involving students.

Risk: Automatic identity creation and local token storage can make account scope and data access hard to audit.

Mitigation: Use only deployments with documented identity boundaries, protected local data storage, token rotation, and a way to disable or scope automatic history queries.

Risk: Insecure HTTP development endpoints and TLS defaults are not suitable for sensitive student data.

Mitigation: Require HTTPS-only production endpoints and remove or disable insecure development endpoints before installation.

Risk: Dependency declaration issues may prevent reliable installation or review.

Mitigation: Correct the dependency declaration and re-scan the release before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include engagement scores, emotion distributions, anonymous seat coordinates, alert levels, teacher suggestions, heatmap/report links, and historical report lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
