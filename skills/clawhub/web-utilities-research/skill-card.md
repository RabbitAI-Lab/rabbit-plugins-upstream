## Description:

General-purpose web-intelligence utilities via the Crawlora API \u2014 scrape any URL to clean markdown/HTML, extract schema-conforming JSON from a page, fingerprint a site's tech stack, geocode addresses, compare cost of living between cities/countries (Numbeo), look up a company's import/export trade records (ImportYeti), check a domain's traffic (SimilarWeb), or resolve a brand's identity from its domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill for one-off public web utility lookups, including page scraping, structured extraction, technology fingerprinting, geocoding, cost-of-living checks, trade-record lookup, traffic lookup, and brand resolution through Crawlora endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs, domains, addresses, and query bodies are sent to Crawlora under the user's API key.

Mitigation: Use only with data that may be shared with Crawlora; avoid secrets, regulated data, and private intranet URLs.

Risk: The helper allows CRAWLORA_API_BASE to override the API base URL.

Mitigation: Use the default Crawlora API base unless the alternate endpoint is trusted.

Risk: Provider datasets such as ImportYeti and SimilarWeb may not be real-time.

Mitigation: Treat returned trade and traffic data as provider-timed research inputs and verify before making high-impact decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/web-utilities-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; calls Crawlora endpoints and returns provider-sourced public web data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
