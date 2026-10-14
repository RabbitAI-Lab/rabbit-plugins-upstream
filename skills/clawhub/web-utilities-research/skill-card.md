## Description:

Provides public web research through Crawlora, including page extraction, site profiling, geocoding, cost-of-living comparisons, trade records, traffic estimates, and brand lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill for one-off public web lookups, such as extracting page content, comparing living costs, and researching companies or domains through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs, including URLs, addresses, and company names, are sent to Crawlora.

Mitigation: Use public, non-sensitive inputs; do not submit private intranet targets, confidential pages, secrets, or sensitive personal data unless sharing is permitted by your policies.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/web-utilities-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON lookup results or a plain-language summary; page scraping can return Markdown or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on public source availability and provider refresh schedules.]

## Skill Version(s):

1.0.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
