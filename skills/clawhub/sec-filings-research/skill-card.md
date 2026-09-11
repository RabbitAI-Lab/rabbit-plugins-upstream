## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora, including company filings, extracted sections, normalized financials, insider transactions, and institutional holdings. Use for sourced filing briefs and period-aware company or disclosure comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, compliance teams, and developers use this skill to research SEC EDGAR filings, compare company disclosures across periods, and prepare sourced filing briefs that preserve entity identifiers, filing metadata, reporting periods, source URLs, and retrieval time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC queries, scrape requests, and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the API key in the environment, use /web/scrape only for relevant public source documents, and avoid sending private or unrelated content through this helper.

Risk: Truncated filing sections, delayed datasets, or degraded enrichments can make evidence incomplete.

Mitigation: Increase extraction caps within documented limits when needed, inspect primary source documents, preserve explicit gaps, and keep data-as-of dates distinct from retrieval time.

Risk: Financial comparisons can be misleading when periods, units, currencies, fiscal calendars, restatements, or XBRL contexts differ.

Mitigation: Preserve fiscal period, end date, currency, units, form, source URL, and taxonomy context; verify comparability before calculating growth, rankings, or disclosure changes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief or comparison with sourced filing details and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish reported facts, management statements, and analytical interpretations; include entity, CIK, accession, form, filing date, reporting period, cited section or fact, source URL, and retrieval time when applicable.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
