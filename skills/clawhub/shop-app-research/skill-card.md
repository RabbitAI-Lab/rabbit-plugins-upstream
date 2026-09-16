## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API, returning clean JSON for cross-store product discovery, merchant comparison, review lookup, and catalog browsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to research public Shop.app products, shops, variants, availability, prices, and reviews through Crawlora instead of scraping Shop.app pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent to Crawlora as a third-party API and may include Shop.app search terms, product identifiers, shop handles, and review lookup targets.

Mitigation: Avoid sending sensitive or private search terms and use the skill for public Shop.app data only.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in command-line arguments.

Mitigation: Keep CRAWLORA_API_KEY in the environment as documented and do not commit or embed it in prompts, scripts, or URLs.

Risk: Successful API calls may consume Crawlora credits.

Mitigation: Use endpoint limits deliberately and prefer summary endpoints such as analysis when a market snapshot is sufficient.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and sends documented Shop.app requests to Crawlora.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
