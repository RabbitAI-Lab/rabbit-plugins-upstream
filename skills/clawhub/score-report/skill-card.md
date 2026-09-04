## Description:

Use when the user wants a claim-safe growth report from validated current evidence, with TrustGrowth score/history when connected and source-specific reporting otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and developers use this skill to prepare forwardable SEO and growth reports from validated current evidence. It supports TrustGrowth-connected reporting when available and source-specific reporting from open or imported evidence otherwise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Forwardable reports can become misleading if unsupported claims, projections, or business attribution are included.

Mitigation: Keep reports limited to validated evidence, observed movement, source scope, and stated limitations; leave missing values missing.

Risk: Paid provider use or third-party SEO indexes can introduce cost and estimate-quality risk.

Mitigation: Review paid provider use before approving batches, label third-party estimates as estimates, and use already-configured read-only connectors when available.

Risk: Connector selection may be incomplete when companion Groundcrew references are unavailable.

Mitigation: Make provider-selection and cost-gated provider guidance available before relying on those connector paths.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with measured values, verdict, next actions, evidence appendix, and not-measured section]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Every reported figure should trace to source, observation time, scope, and limitations; missing values remain missing.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
