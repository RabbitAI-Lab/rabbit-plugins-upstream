## Description:

Fetches structured public web data via the Crawlora REST API - search engines, e-commerce, social, finance, maps, app stores, media, and reviews - returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs live, structured data from public websites without maintaining browser automation, proxies, or HTML parsers. Common tasks include comparing product prices, retrieving transcripts or reviews, checking search results and trends, and querying public finance, maps, app store, media, or social data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key and request data to a non-default API base if CRAWLORA_API_BASE is changed.

Mitigation: Keep CRAWLORA_API_BASE unset or explicitly pinned to https://api.crawlora.net/api/v1 before running the helper.

Risk: Public website lookup prompts or results may be sent through Crawlora.

Mitigation: Use the skill only for public website data and avoid submitting secrets, private URLs, or internal identifiers.

Risk: Monitor endpoints can create ongoing remote checks when intentionally used.

Mitigation: Use monitor endpoints only when persistent checks are required and document the expected monitoring scope.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora skill page](https://clawhub.ai/tonywangcn/skills/crawlora)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; the helper prints raw JSON for downstream parsing.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
