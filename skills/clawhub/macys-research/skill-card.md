## Description:

Looks up Macy's product details, customer reviews, and typeahead suggestions through the Crawlora API using a known numeric product ID or suggestion query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public Macy's product details, customer review summaries, paginated reviews, and search-box suggestions through Crawlora without scraping Macy's pages directly. It is intended for workflows where the user already has a Macy's product page ID, because it does not provide full product search or category browsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and can spend Crawlora credits for product lookups.

Mitigation: Install only when comfortable granting the helper access to CRAWLORA_API_KEY and spending Crawlora credits; keep the key in the environment and do not hardcode or commit it.

Risk: Security evidence flags the credentialed curl wrapper as under-scoped and recommends review.

Mitigation: Avoid untrusted or nonnumeric product IDs; the publisher should tighten productId validation to digits only, disable curl globbing, and reject POST for this GET-only skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/macys-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known Macy's numeric product ID for product detail and review lookups; typeahead suggestions require a query string.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
