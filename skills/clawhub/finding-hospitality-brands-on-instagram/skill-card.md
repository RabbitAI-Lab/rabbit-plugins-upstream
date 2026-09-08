## Description:

Discovers hotels, travel brands, resorts, and hospitality businesses on Instagram using apidojo's Instagram Scraper on Apify, returning account handles, follower counts, bios, and per-post engagement data for hospitality prospecting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, marketing, and business-development users use this skill to find and rank hotels, resorts, travel brands, and hospitality businesses on Instagram for B2B outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected Instagram URLs and scrape parameters to Apify and depends on an APIFY_TOKEN for service access.

Mitigation: Install and run it only where use of Apify for Instagram scraping is approved, and keep the APIFY_TOKEN managed as a service credential.

Risk: Scraped Instagram data used for outreach may be subject to Apify and Instagram terms or internal data-use policies.

Mitigation: Review Apify and Instagram terms, plus applicable outreach and privacy requirements, before building or using prospecting datasets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-hospitality-brands-on-instagram)
- [Apify Instagram Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~instagram-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, REST API examples, JSON input, CSV or JSON output options, and scoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate outreach datasets containing Instagram account metadata and engagement-derived prospect scores.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
