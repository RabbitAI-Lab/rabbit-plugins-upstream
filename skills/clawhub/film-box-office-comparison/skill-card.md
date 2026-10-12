## Description:

Compare theatrical film grosses through Crawlora Box Office Mojo charts, title and release records, and stored data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to compare theatrical grosses across films, release windows, markets, or franchises while preserving reporting basis, dates, and source coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Box-office lookup parameters and the Crawlora API key are sent to Crawlora.

Mitigation: Use a Crawlora-scoped key and omit unrelated private information from queries.

Risk: Broad lookups can consume API credits.

Mitigation: Limit searches and pages to the requested scope and monitor credit usage.

Risk: Mixing lifetime, reissue, estimate, or differently dated grosses can mislead comparisons.

Mitigation: Keep release identity, reporting basis, currency, dates, and missing coverage explicit; compare like-for-like figures.

## Reference(s):

- [Film box office comparison on ClawHub](https://clawhub.ai/crawlora-org/skills/film-box-office-comparison)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown comparison table and identity/release ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, reporting dates, gross figures, calculation basis, and missing-data notes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
