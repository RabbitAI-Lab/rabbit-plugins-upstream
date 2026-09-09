## Description:

Fetches structured public web data via the Crawlora REST API \u2014 search engines, e-commerce, social, finance, maps, app stores, media, and reviews \u2014 returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Crawlora to fetch live, structured JSON from public websites for search results, product prices, reviews, transcripts, trends, financial data, places, and similar public-web research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public search terms, URLs, endpoint parameters, and the Crawlora API key are sent to the configured Crawlora API service.

Mitigation: Use only public, non-sensitive inputs; do not submit private URLs, authenticated pages, secrets, proprietary files, or sensitive personal data.

Risk: The helper supports overriding the API base, which could expose request data or the API key to an unexpected service.

Mitigation: Before use, verify CRAWLORA_API_BASE is unset or exactly the official Crawlora API base, and rotate the key if the skill may have run in an untrusted environment.

## Reference(s):

- [Crawlora endpoint catalog](artifact/reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; API calls return raw JSON for downstream parsing.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
