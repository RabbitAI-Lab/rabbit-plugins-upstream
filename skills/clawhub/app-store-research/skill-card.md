## Description:

Researches public app and browser-extension listings across the Apple App Store, Google Play, and Chrome Web Store using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and product teams use this skill to discover and compare public app and extension listings, reviews, ratings, permissions, privacy disclosures, and release histories across stores.

### Deployment Geography for Use:

Global; listing availability and reviews vary by country and language.

## Known Risks and Mitigations:

Risk: Search terms, app identifiers, and API usage are sent to Crawlora.

Mitigation: Avoid private data in queries and use the skill only if sharing those queries with Crawlora is acceptable.

Risk: Review samples and listing disclosures can be incomplete or misleading when treated as population sentiment or independent security findings.

Mitigation: Preserve source, country, language, and sampling details; treat permissions and privacy statements as reported disclosures.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/app-store-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Comparative summaries with structured public listing data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Store, country, language, and review-sampling context should accompany comparisons.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
