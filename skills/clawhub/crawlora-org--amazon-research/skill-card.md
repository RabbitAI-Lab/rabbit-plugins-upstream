## Description:

Researches Amazon products, pricing, availability, and search suggestions through the Crawlora API without scraping Amazon pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, analysts, and developers use the skill to find Amazon listings, check product prices and availability by ASIN, and explore search suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon search terms, ASINs, and request parameters are sent to Crawlora.

Mitigation: Use only for public Amazon research; do not submit private or non-Amazon data.

Risk: The Crawlora API key is required for requests.

Mitigation: Keep the key in CRAWLORA_API_KEY and never place it in commands, query parameters, or committed files.

## Reference(s):

- [Amazon endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/amazon-research)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Natural-language product research or JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Amazon.com results can be paginated; API access requires a Crawlora key.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
