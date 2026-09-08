## Description:

Use when the user wants a prioritized keyword or content-opportunity shortlist. Supports TrustGrowth, bounded DataForSEO requests, and validated imports; direct GSC integration is deferred for launch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External users, SEO teams, and content operators use this skill to produce a short prioritized list of keyword or content opportunities from validated imports, TrustGrowth data, or bounded SEO provider requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO queries and site data may be shared with configured third-party SEO providers.

Mitigation: Confirm provider data-sharing expectations before installation or use.

Risk: Paid DataForSEO batches can incur cost.

Mitigation: Require explicit cost approval before each billable batch.

Risk: Two referenced guidance files are missing from the release evidence.

Mitigation: Use extra review before paid provider runs and confirm required guidance is present in a future release.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance, configuration]

**Output Format:** [Markdown shortlist with evidence labels, limitations, and recommended next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns 5-10 recommendations and keeps unknown volume or position values unknown.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
