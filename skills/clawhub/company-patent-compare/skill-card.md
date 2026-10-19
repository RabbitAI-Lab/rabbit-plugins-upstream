## Description:

Compares patents held by two to five companies, including portfolio size, legal status, filing trends, and overlapping technology areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, investors, and competitive analysts compare the patent portfolios of two to five named companies and receive a spreadsheet-ready comparison with a short interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, patent queries, and supplied technical descriptions are sent to PatentMax.

Mitigation: Do not submit unpublished inventions, source code, formulas, or trade secrets unless organizational policy permits this service.

Risk: The skill stores trial credentials, task budgets, ledgers, and caches on the local machine.

Mitigation: Review local storage and credential handling before use; provide an API key only to a trusted PatentMax endpoint and avoid changing the API destination unless you control it.

Risk: Patent comparison requests may incur API charges, and portfolio counts alone can overstate technical strength.

Mitigation: Confirm estimated costs before paid queries and treat the comparison as a screening aid rather than a legal or technical-strength conclusion.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/company-patent-compare)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax patent search](https://app.ip930.com)
- [PatentMax API reference included with the skill](artifact/references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, CSV, Guidance]

**Output Format:** [UTF-8 CSV with BOM and a plain-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares two to five companies; includes source and comparison date.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
