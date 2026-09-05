## Description:

Use when the user wants an E-E-A-T, credibility, authorship, or trust-signal review using TrustGrowth evidence when connected or observable public/repository evidence otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, SEO practitioners, and developers use this skill to review E-E-A-T, credibility, authorship, and trust signals from TrustGrowth measurements when connected, or from observable public site and repository evidence otherwise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected provider use can involve configured credentials, paid services, and data sharing with SEO or analytics providers.

Mitigation: Use connected sources only when already configured and appropriate for the site owner; review provider costs, scopes, and data-sharing terms before approving those runs.

Risk: Credibility reviews can become misleading if missing data is filled in, identities or credentials are invented, or unverifiable score changes are promised.

Mitigation: Trace claims to validated evidence, keep null or unmeasured values explicit, refuse fabricated trust signals, and avoid score-change predictions.

Risk: Outward-facing publishing or irreversible changes based on the review could affect site trust claims.

Mitigation: Separate code-fixable, content-fixable, and structural recommendations, and require owner review before publishing or irreversible changes.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with evidence-backed findings and recommended actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend at most one missing connector; preserves unknown values as unknown and does not predict score changes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
