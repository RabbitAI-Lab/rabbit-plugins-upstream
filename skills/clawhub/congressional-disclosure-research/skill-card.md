## Description:

Researches public House and Senate financial-disclosure filings through Crawlora and prepares filing inventories or transaction evidence briefs from supported reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and other users can inventory public congressional financial-disclosure filings and prepare source-linked transaction evidence briefs while retaining uncertainty about dates, amounts, duplicates, and unavailable documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup parameters and the user's API key are sent to Crawlora.

Mitigation: Use a scoped, private API key and install only if comfortable sharing the lookup parameters with Crawlora.

Risk: Incomplete document parsing, overlapping reports, and amount ranges can lead to misleading conclusions.

Mitigation: Preserve source links and date and range labels, mark unsupported documents unavailable, and label probable duplicates without treating them as proven matches.

## Reference(s):

- [Disclosure endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/congressional-disclosure-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Filing coverage, source-linked transaction evidence, unavailable documents, possible duplicates, and date and amount-range limitations.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
