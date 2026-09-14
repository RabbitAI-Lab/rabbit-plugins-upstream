## Description:

Researches Lululemon's catalog - category navigation, category listings, product detail with pricing, sizes, reviews, curated outfit recommendations, and the physical store directory - using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public Lululemon catalog, product, outfit, review, availability, pricing, and store-directory data through Crawlora instead of scraping shop.lululemon.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-requested lookup parameters to Crawlora.

Mitigation: Use it only for Lululemon catalog, product, outfit, review, availability, pricing, and store-directory requests that users are comfortable sharing with Crawlora.

Risk: The Crawlora API key could be exposed if copied into prompts, files, command history, or URLs.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not hardcode or commit it, and use the bundled helper that keeps the key out of command-line arguments.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/lululemon-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized public Lululemon data from documented Crawlora endpoints.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
