## Description:

Researches Zappos footwear and apparel catalog data, including brand listings, product search, pricing, images, ratings, fit feedback, and color variants, through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and compare public Zappos catalog data without scraping zappos.com. It supports brand discovery, catalog browsing, product lookup, and fit or variant due diligence for footwear and apparel research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zappos search terms, brand identifiers, product IDs, color IDs, and related query parameters are sent to Crawlora.

Mitigation: Avoid private or sensitive information in search terms and request bodies; use the skill only for intended public catalog research.

Risk: Crawlora API access depends on the CRAWLORA_API_KEY secret.

Mitigation: Keep CRAWLORA_API_KEY in the environment and out of committed files, command arguments, and shared transcripts.

## Reference(s):

- [Zappos endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub zappos-research skill page](https://clawhub.ai/crawlora-org/skills/zappos-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses paginated Zappos brand, search, suggest, and product-detail endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
