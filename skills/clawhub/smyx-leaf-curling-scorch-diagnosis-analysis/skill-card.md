## Description:

Uses plant leaf images or videos, with optional soil-moisture context, to identify curling direction, leaf-margin scorch patterns, affected leaf layers, and likely causes such as drought stress, disease, pesticide damage, fertilizer burn, or cold stress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External agricultural operators, agronomists, and developers use this skill to triage plant leaf curling and margin scorch from field, greenhouse, orchard, UAV, or mobile-app imagery. It returns structured observations, likely-cause ranking, directional recommendations, and optional historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant media or URLs to a backend service.

Mitigation: Use it only where sending the submitted imagery or URLs to the configured service is acceptable.

Risk: The skill can query cloud-stored history and silently create or reuse an internal identity.

Mitigation: Review identity and history-query behavior before installation, especially in shared or regulated environments.

Risk: The skill stores service tokens in a workspace SQLite database.

Mitigation: Install it only in workspaces where local token storage is acceptable and access to the workspace is controlled.

Risk: The bundled configuration includes private development endpoints.

Mitigation: Verify the API configuration points to the intended production service before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-curling-scorch-diagnosis-analysis)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown and JSON analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save structured results to a file when an output path is provided.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
