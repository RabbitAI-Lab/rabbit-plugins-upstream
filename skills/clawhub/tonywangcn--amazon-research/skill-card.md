## Description:

Amazon Research helps agents look up Amazon.com products, prices, availability, and search suggestions through the Crawlora API and return normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill for Amazon.com product research, including product search, ASIN detail lookup, price and availability checks, and autocomplete keyword discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can call non-Amazon Crawlora endpoints and relay caller-provided JSON request bodies beyond the advertised Amazon research scope.

Mitigation: Restrict use to /amazon/search, /amazon/product/{asin}, and /amazon/suggest/{keyword}; review commands before execution and prefer an updated version with an endpoint allowlist.

Risk: Requests are sent to external Crawlora API endpoints using the caller's API key.

Mitigation: Do not include sensitive data in paths, query parameters, or JSON bodies; keep CRAWLORA_API_KEY in the environment only and rotate it if exposed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Amazon search responses are paginated.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
