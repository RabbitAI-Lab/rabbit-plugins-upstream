## Description:

Use when the user wants a generative-engine-optimization report - whether AI systems can reach, read, retrieve, and recall the site - as a document, from public checks or the TrustGrowth visibility funnel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, marketers, and SEO engineers use this skill to produce a dated GEO report that summarizes whether AI systems can reach, read, retrieve, and recall a site. The report packages public checks or the TrustGrowth visibility funnel into a document with evidence labels, a verdict, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed or paid SEO connectors may access account data or incur costs if approved.

Mitigation: Use only connectors the user has already configured and intends to use, confirm paid or credentialed access before running, and never expose API keys.

Risk: Unsupported or unvalidated evidence could make a GEO report misleading.

Mitigation: Validate normalized factual inputs before drawing conclusions, label unavailable data as not measured, and avoid estimating missing funnel stages.

## Reference(s):

- [Connectors and Categories](references/connectors.md)
- [Reporting Contract](references/reporting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with evidence labels, a verdict, measured findings, next actions, evidence, and not-measured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SHIP/FIX/BLOCK/UNDECIDED verdicts and Measured/User-provided/Estimated labels.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
