## Description:

Use when the user wants a current site audit, technical SEO findings, Core Web Vitals interpretation, or a fresh TrustGrowth audit when connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site owners use this skill to audit public, imported, or connected site evidence; interpret technical SEO and Core Web Vitals findings; and identify prioritized next actions without inventing missing measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may query public pages and user-configured SEO services during an audit.

Mitigation: Only use paid or credentialed connectors the user already trusts, and keep unobserved data marked as unknown.

Risk: Manual TrustGrowth audits can require write scope, plan support, and explicit user intent.

Mitigation: Confirm the user's request before triggering an audit, respect rate-limit responses, and avoid stacking retries.

Risk: Imported or public audit evidence can be stale, incomplete, or difficult to compare across sources.

Mitigation: Report source and observation date, separate lab from field evidence, and avoid comparing unlike measurements.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with evidence-labeled findings, verdicts, next actions, and optional shell commands for local evidence validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should separate observed facts from interpretation, label missing data as unknown, and avoid score-impact projections.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
