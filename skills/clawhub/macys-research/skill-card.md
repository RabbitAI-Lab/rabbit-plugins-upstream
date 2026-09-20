## Description:

Looks up Macy's product details, customer reviews, and typeahead suggestions through the Crawlora API, returning clean JSON for known numeric product IDs or suggestion queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve public Macy's product detail, review summaries, paginated reviews, and autocomplete suggestions through Crawlora when they already have a product ID or suggestion query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested Macy's product IDs, review queries, and suggestion queries to Crawlora as a third-party API provider.

Mitigation: Install and use it only when Crawlora's terms and privacy expectations fit the deployment use case.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed directly in commands.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the provided helper, which is documented to keep the key out of command-line arguments.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/macys-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance, Configuration]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment and a documented Macy's product ID or suggestion query.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
