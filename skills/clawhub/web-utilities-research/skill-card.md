## Description:

General-purpose web-intelligence utilities via the Crawlora API: scrape public URLs to clean markdown or HTML, extract schema-conforming JSON from pages, fingerprint website technology stacks, geocode addresses, compare cost of living, look up trade records, check site traffic, and resolve brand identity from domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agent users use this skill for one-off public web research tasks through Crawlora API calls, including page extraction, technology detection, geocoding, cost-of-living comparison, trade-record lookup, site-traffic lookup, and brand metadata retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup targets, URLs, addresses, domains, request payloads, and similar inputs are sent to the Crawlora API.

Mitigation: Do not use this skill with secrets, internal URLs, confidential targets, access tokens, or sensitive personal addresses unless third-party disclosure to Crawlora is acceptable.

Risk: The skill retrieves public web, geocoding, cost-of-living, trade-record, traffic, and brand data that may be incomplete, stale, or governed by source-site terms.

Mitigation: Use outputs as research assistance, respect site terms and robots directives, and verify important results against authoritative sources before relying on them.

Risk: The helper requires a Crawlora API key and makes external network requests.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, do not hardcode or commit it, and install only when external requests to Crawlora are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/web-utilities-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper sends requests to Crawlora endpoints and returns raw JSON suitable for summarization or downstream parsing.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
