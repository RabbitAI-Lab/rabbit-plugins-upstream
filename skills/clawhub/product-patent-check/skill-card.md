## Description:

Finds a brand's product-related patents across company name variants and organizes inventions, utility models, and designs by component.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, sellers, and competitive researchers use it to identify patents associated with a brand's product, compare protected components, and review notable claims. It does not determine whether a specific product infringes a patent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries may disclose product details or confidential technical information to PatentMax/ip930.

Mitigation: Avoid submitting trade secrets unless that service relationship is acceptable.

Risk: Patent searches and detailed reads may incur API charges.

Mitigation: Confirm the expected cost before searching and monitor paid API usage.

Risk: API credentials and local task or key caches require care.

Mitigation: Keep PATENTMAX_API_KEY private, use only a trusted PATENTMAX_BASE_URL endpoint, and protect local caches under ~/.patentmax.

Risk: Patent search results may not identify patents used by a specific product model or establish infringement.

Mitigation: Present results as product-related leads, verify important records, and do not offer infringement conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/product-patent-check)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Query syntax](artifact/references/query-syntax.md)
- [Search workflow](artifact/references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [Markdown summary and Excel-compatible CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CSV groups patents by component and includes publication number, applicant, filing date, legal status, and a brief description of protection.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
