## Description:

General-purpose web-intelligence utilities via the Crawlora API: scrape URLs to clean markdown or HTML, extract schema-conforming JSON from a page, fingerprint a site's tech stack, geocode addresses, compare cost of living, look up import/export trade records, check domain traffic, and resolve brand identity from a domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill for one-off public web research tasks such as scraping a URL, extracting structured page data, checking a website's technology stack or traffic, resolving geocoding data, comparing cost of living, and researching company trade records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs such as URLs, domains, addresses, schemas, and research queries are transmitted to Crawlora and may involve third-party data sources.

Mitigation: Use only public, non-sensitive inputs unless disclosure to Crawlora and the referenced data providers is approved under your policies.

Risk: Web, traffic, import/export, and cost-of-living data can be incomplete, stale, or governed by provider refresh cycles.

Mitigation: Treat returned data as research support and verify important decisions against authoritative or primary sources.

Risk: The helper requires an API key for an external service.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not hardcode or commit it, and rotate it if exposure is suspected.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora Documentation](https://crawlora.net/docs)
- [Crawlora Playground](https://crawlora.net/playground)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/web-utilities-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, shell commands, and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
