## Description:

Use when the user wants a periodic competitor digest that shows what tracked competitors changed and where gaps exist, using observation history or public diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

SEO and growth teams use this skill to produce competitor readouts from public page diffs, prior crawl history, user-configured SEO providers, or TrustGrowth observation history. The report highlights observed changes, content gaps, evidence labels, and next actions without presenting third-party estimates as measured competitor facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full functionality may depend on Groundcrew support files being present.

Mitigation: Confirm the referenced Groundcrew files are available before expecting evidence validation workflows to run.

Risk: Configured SEO providers such as Ahrefs, Semrush, DataForSEO, or TrustGrowth may incur per-request or account costs.

Mitigation: Use paid providers only when the user has intentionally configured the account and understands the cost impact.

Risk: Competitor traffic, ranking, or keyword claims from third-party indexes can be mistaken for measured facts.

Mitigation: Label third-party values as Estimated with the estimator named, and require owner review before outward-facing competitor comparisons.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)
- [ClawHub skill page](https://clawhub.ai/trustgrowth/skills/competitor-readout)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands]

**Output Format:** [Markdown report with evidence labels, verdicts, tables, and concise next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands for validating evidence records and may reference configured SEO providers or public-page observations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
