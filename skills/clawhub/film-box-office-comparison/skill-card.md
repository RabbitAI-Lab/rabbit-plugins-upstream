## Description:

Compare theatrical film grosses through Crawlora Box Office Mojo charts, title/release records, and stored data, preserving the title, release, currency, and reporting basis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to compare theatrical grosses across films, release windows, markets, and franchises, with clear sourcing and consistent reporting bases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie titles, search queries, Box Office Mojo URLs, and request metadata are sent to Crawlora.

Mitigation: Use the skill only when sharing that research data with Crawlora is acceptable; limit requests to the needed scope.

Risk: Disclosure of the Crawlora API key could expose the user's account.

Mitigation: Keep CRAWLORA_API_KEY private and do not include it in reports or shared requests.

Risk: Mixing estimates, reissues, reporting dates, or geographic totals can distort comparisons.

Mitigation: Compare like-for-like figures and retain dates, release scope, currency, sources, and missing-data labels.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/film-box-office-comparison)
- [Box-office endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison table and identity/release ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and dates, gross figures, formulas, scope, coverage, and missing fields.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
