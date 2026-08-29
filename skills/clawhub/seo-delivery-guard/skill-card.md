## Description:

Govern SEO findings and requirements through implementation, review, release gates, regression repair, and production verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangxin12345](https://clawhub.ai/user/pangxin12345)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release owners, and SEO-focused agents use this skill to turn accepted SEO audit findings or search-facing requirements into scoped implementation, review, release-gate, regression-repair, and production-verification work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad access to private SEO, analytics, repository, or customer data could expose sensitive information.

Mitigation: Provide only the specific repository paths, public URLs, sanitized evidence, and separately authorized external properties needed for the task; do not provide secrets, credentials, cookies, or broad analytics exports.

Risk: SEO guidance can be mistaken for permission to deploy, publish, submit URLs, alter search properties, or make account changes.

Mitigation: Treat analysis as read-only unless the user separately authorizes implementation or a specific external write immediately before that action.

Risk: Search-engine outcomes such as indexing, ranking, traffic, rich results, advertising approval, or AI citations may be reported as guaranteed or already achieved.

Mitigation: Report engineering verification separately from delayed external outcomes, and keep unverified search-platform state pending until confirmed through authorized first-party or public checks.

## Reference(s):

- [SEO Delivery Guard on ClawHub](https://clawhub.ai/pangxin12345/skills/seo-delivery-guard)
- [Publisher Profile](https://clawhub.ai/user/pangxin12345)
- [Official Website](https://once-email.com)
- [Capability orchestration](references/orchestration.md)
- [Evidence and severity](references/evidence-and-severity.md)
- [Project policy adapters](references/project-policy-adapters.md)
- [SEO delivery gates](references/delivery-gates.md)
- [Google Search boundaries](references/google-search-boundaries.md)
- [Content and indexability](references/content-and-indexability.md)
- [Data and measurement](references/data-and-measurement.md)
- [Search-platform boundaries](references/search-platform-boundaries.md)
- [Usage and safety](references/usage-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only governance output; external writes, deployments, submissions, and account changes require separate explicit authorization.]

## Skill Version(s):

0.1.2 (source: frontmatter, changelog, and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
