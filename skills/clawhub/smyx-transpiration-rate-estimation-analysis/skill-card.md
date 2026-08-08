## Description:

Estimates an indoor plant transpiration-rate index from thermal or RGB leaf imagery and optional environmental data, returning water-stress, root-vigor, and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze indoor plant leaf images or videos, estimate relative transpiration rate, and review structured guidance about water stress, root water-uptake activity, and care direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media, URLs, and report queries may be sent to lifeemergence.com or open.lifeemergence.com services.

Mitigation: Use only inputs appropriate for that remote processing path, and avoid files or URLs that contain sensitive content or embedded secrets.

Risk: The skill can automatically create or reuse a local identity and persist service tokens in a workspace SQLite database.

Mitigation: Review or clear the workspace data directory when account linkage should not persist, and treat stored tokens as sensitive local data.

Risk: The release includes generic or pet-health components that may not match the plant transpiration use case.

Mitigation: Review generated reports and service behavior before relying on the skill for operational plant-care decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON analysis report with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a transpiration-rate index, root-vigor assessment, stress indicators, care suggestions, and a historical report table.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
