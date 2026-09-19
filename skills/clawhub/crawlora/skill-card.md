## Description:

Fetches structured public web data via the Crawlora REST API — search engines, e-commerce, social, finance, maps, app stores, media, and reviews — returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured public web data for product research, search results, reviews, transcripts, financial lookups, maps, app stores, media, and social web tasks that would otherwise require custom scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-requested lookup terms, URLs, IDs, and request bodies are sent to Crawlora.

Mitigation: Use the skill only for public-web lookups and avoid secrets, private/internal URLs, personal data, or account-specific workflows.

Risk: The Crawlora API key could be exposed if placed in prompts, files, URLs, or command history.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the bundled helper, which avoids putting the key directly on the curl command line.

Risk: Some public-web source endpoints may fail or return upstream challenge responses.

Mitigation: Handle non-2xx responses, retry when appropriate, or fall back to another documented provider endpoint.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with shell commands and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; API responses contain structured public web data.]

## Skill Version(s):

1.0.24 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
