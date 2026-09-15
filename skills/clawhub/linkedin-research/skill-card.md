## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve public LinkedIn company, product, or showcase page data by known ID for company enrichment, competitor profiling, product-page audits, and showcase-page checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends requested LinkedIn company, product, or showcase IDs to Crawlora.

Mitigation: Use only intended public IDs, keep CRAWLORA_API_KEY in environment-managed secrets, and confirm users are comfortable with Crawlora API use before running requests.

Risk: The helper allows POST even though the documented LinkedIn endpoints are GET calls.

Mitigation: Prefer the documented GET calls and avoid POST unless the publisher documents POST behavior for these endpoints.

## Reference(s):

- [LinkedIn endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known LinkedIn company, product, or showcase page ID.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
