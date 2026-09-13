## Description:

Researches Kohl's catalog by browsing its category taxonomy, pulling product reviews by web_id, finding nearby Kohl's stores, and returning search-box typeahead suggestions via the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Kohl's catalog, review, suggestion, and store-location data through Crawlora instead of scraping Kohls.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kohl's lookup terms, product IDs, and store-search locations to Crawlora.

Mitigation: Use only lookup data you are comfortable sharing with Crawlora, and prefer city or ZIP over a full address unless a precise store lookup is needed.

Risk: The skill depends on a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment and out of code, command-line arguments, commits, and shared logs.

## Reference(s):

- [Kohl's endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/kohls-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends selected Kohl's lookup terms, product IDs, and store-search locations to Crawlora.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
