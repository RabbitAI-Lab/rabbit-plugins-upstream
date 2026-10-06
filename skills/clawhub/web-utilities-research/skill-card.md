## Description:

Provides web scraping, structured extraction, site technology and traffic lookups, geocoding, cost-of-living data, trade records, and brand information through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can investigate public websites, locations, companies, and brands through one-off Crawlora lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs, query parameters, and JSON request bodies are sent to Crawlora.

Mitigation: Use public, non-confidential targets; do not send secrets, internal URLs, regulated personal data, or proprietary content without reviewing Crawlora's data handling terms.

Risk: Third-party traffic and trade data may be outdated or incomplete.

Mitigation: Check the source and freshness of consequential findings before relying on them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/web-utilities-research)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Skill endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown responses or structured JSON, depending on the request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scraped content may be returned as Markdown or HTML; lookup results are supplied as JSON.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
