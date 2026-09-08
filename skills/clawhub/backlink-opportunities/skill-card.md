## Description:

Use when the user asks about backlinks, referring domains, link building, broken links pointing at them, or link gaps versus competitors. Analyzes a backlink profile and produces a human-reviewed link-opportunity plan: reclamation, competitor intersection, linkable assets, and unlinked mentions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, site owners, and marketing teams use this skill to analyze backlink data and produce a human-reviewed opportunity plan for link reclamation, competitor intersections, linkable assets, and unlinked mentions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backlink providers and third-party indexes can be incomplete or provider-specific.

Mitigation: Keep provider name, retrieval date, and limitations on every profile fact; label missing coverage as not measured rather than estimating.

Risk: Paid SEO providers or backlink endpoints may incur costs.

Mitigation: Run an explicit cost preflight and obtain approval before using any paid provider calls.

Risk: Outreach, redirects, and disavow actions can have external or irreversible effects.

Mitigation: Keep outputs as plans and draft angles; require human owner review before outreach, redirects, or any disavow-related decision.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with prospect tables, evidence references, draft angles, not-measured notes, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces advisory backlink opportunity plans only; outreach, redirects, and disavow decisions remain under human review.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
