## Description:

Organizes Amazon review pain points, product fields, and usage context into verifiable product requirements and acceptance questions; it does not make engineering schedule, procurement, purchasing, sales, or profit commitments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product managers, and operators use this skill to convert Amazon review evidence and product fields into actionable product requirements and acceptance questions. It is intended for requirements analysis, not execution of engineering schedules, procurement, sales forecasting, or profit prediction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced CLI overrides can steer paid operations outside the advertised product-requirements scope.

Mitigation: Do not use or allow `--workflow` or `--focus` overrides; keep use to the documented `product/requirements` workflow until the publisher closes this boundary.

Risk: The skill stores an ARI API key locally and can check account and credit data.

Mitigation: Use a scoped ARI key where available, protect the local environment where the key is stored, and run account checks only in trusted workspaces.

Risk: Collection and analysis may spend ARI credits.

Mitigation: Run quote/profile steps first and proceed only after explicit user confirmation with the same request ID.

## Reference(s):

- [Product Requirements Skill Listing](https://clawhub.ai/funewa/skills/product-requirements)
- [Amazon Product Requirements Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Product Requirements API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and ARI API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis actions require a quote and explicit user confirmation before credits are spent.]

## Skill Version(s):

1.4.11 (source: evidence.release, artifact/_meta.json, artifact/CHANGELOG.md, artifact/scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
