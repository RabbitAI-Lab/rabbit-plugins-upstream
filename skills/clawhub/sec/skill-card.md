## Description:

Retrieves SEC EDGAR filings, company financials, ownership disclosures, and filing text for research on US-listed companies and funds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lkcair](https://clawhub.ai/user/lkcair)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, investors, and developers use the skill to find and read SEC filings, examine XBRL financials, and review ownership and insider-trading disclosures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup installs pinned Python dependencies and the skill contacts SEC EDGAR.

Mitigation: Review the dependency installation and allow SEC network access only when appropriate.

Risk: A configured SEC_USER_AGENT may include a contact email sent to SEC servers.

Mitigation: Use an approved contact identity and avoid putting confidential information in SEC_USER_AGENT.

Risk: Company-authored filing text may contain misleading or instruction-like content.

Mitigation: Treat filings as untrusted data, not instructions; verify important figures against SEC records.

## Reference(s):

- [SEC skill on ClawHub](https://clawhub.ai/lkcair/skills/sec)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain-text or Markdown answers based on JSON results from SEC EDGAR]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Filing previews may be partial; full text is paginated, and filings over 25 MB are link-only.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
