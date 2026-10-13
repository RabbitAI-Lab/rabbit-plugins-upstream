## Description:

Compare app review themes around documented releases using Crawlora version notes and live or stored reviews, preserving release identity, sampling, missing history, and causal limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to compare app review themes around documented iOS or Android releases and produce a dated feedback brief with clearly identified samples and attribution limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App IDs, review queries, and an API key are sent to Crawlora.

Mitigation: Use this skill only if that data transfer is acceptable; protect the API key and limit queries to the requested app and storefront.

Risk: Broad review searches can consume credits or yield biased comparisons.

Mitigation: Bound calls to the requested date window and credit budget, and disclose sample selection and version-attribution limits.

## Reference(s):

- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/app-release-feedback-analysis)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Markdown release-feedback brief with tables and cited review excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes release and attribution ledger, sample counts, missing data, and follow-up hypotheses.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
