## Description:

Builds evidence-only Kimball semantic layers from REST/OpenAPI, CLI, or table/database interfaces through an HTML decision workbench, then emits Google OKF or repository YAML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to convert interface contracts into governed semantic models for enterprise knowledge modeling, semantic layers, dimensional models, ontology, or OKF. It supports a gated workflow for ingesting evidence, reviewing decisions, emitting OKF or YAML artifacts, and verifying structural and semantic constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML review reports can execute script from hostile source data when model JSON is embedded without HTML-safe escaping.

Mitigation: HTML-escape embedded JSON or load the model from a separate JSON file before using the workflow with untrusted or third-party contracts.

Risk: Incomplete or ambiguous interface evidence can lead to TODO(verify) placeholders or blocked decisions rather than a completed semantic model.

Mitigation: Require Phase 2 review approval with no open or blocked decisions before emitting OKF or repository YAML artifacts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/semantic-km-creator)
- [OpenClaw Homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/semantic-km-creator)
- [Ingest Workflow](artifact/references/ingest.md)
- [Decision Review Workflow](artifact/references/review.md)
- [Google OKF Emit Workflow](artifact/references/emit-okf.md)
- [Repository YAML Emit Workflow](artifact/references/emit-yaml.md)
- [Verification Workflow](artifact/references/verify.md)
- [Worked Example](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, HTML review reports, OKF bundles, repository YAML, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated semantic artifacts must remain evidence-backed; unsupported fields are marked TODO(verify) or held as open decisions.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact metadata reports 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
