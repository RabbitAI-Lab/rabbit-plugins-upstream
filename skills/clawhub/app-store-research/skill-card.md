## Description:

Researches apps and browser extensions across the Apple App Store, Google Play, and Chrome Web Store using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to discover and compare public app and browser-extension listings, reviews, ratings, permissions, privacy disclosures, rankings, and release history across major app stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store queries and the Crawlora API key are sent to Crawlora.

Mitigation: Install and run this skill only when sending those queries and credentials to Crawlora is acceptable.

Risk: Returned reviews, privacy disclosures, permissions, and publisher contact fields are public-source research data, not a security audit.

Mitigation: Treat results as listing evidence, preserve source context, and handle personal or business contact details with care.

Risk: A selected review sample, ranking, or review count can misrepresent population sentiment, downloads, revenue, retention, or market share.

Mitigation: Report locale, language, sort, page, and source, and avoid inferring market metrics that the evidence does not support.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-store-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public store listing data returned by Crawlora endpoints.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
