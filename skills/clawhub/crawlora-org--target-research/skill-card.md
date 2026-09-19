## Description:

Researches Target catalog categories, products, filters, prices, questions, and reviews through the Crawlora API and returns normalized JSON for product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search or browse Target products, compare pricing and availability by store, and summarize product questions or reviews without scraping target.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target search terms, item IDs, and optional store IDs are sent to Crawlora.

Mitigation: Do not include sensitive personal information in product queries, and use the skill only when sending the requested shopping data to Crawlora is acceptable.

Risk: The Crawlora API key could be exposed if copied into files, prompts, command arguments, or logs.

Mitigation: Keep CRAWLORA_API_KEY in the environment; the bundled helper sends it through a temporary curl config rather than command-line parameters.

Risk: Target product results are paginated and store-specific pricing or availability can vary by store_id.

Mitigation: Page through result sets when coverage matters and pass the intended store_id for local price or availability comparisons.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/target-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with concise Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API key authentication from the CRAWLORA_API_KEY environment variable.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
