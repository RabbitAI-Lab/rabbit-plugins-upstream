## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and go-to-market teams use this skill to retrieve public LinkedIn company, product, and showcase data through Crawlora for firmographic research, competitor profiling, and record enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential LinkedIn research terms may be sent to Crawlora.

Mitigation: Use this skill only where Crawlora is an approved processor for the intended data, and avoid sensitive research terms unless that processing is permitted.

Risk: The helper exposes product search and category routes even though the main instructions emphasize ID-only lookups.

Mitigation: Review the endpoint reference before use and restrict calls to company, product, and showcase ID routes when broader product search is not approved.

Risk: The skill requires a Crawlora API key.

Mitigation: Store CRAWLORA_API_KEY in an approved secret manager or environment configuration, and do not hardcode or commit it.

## Reference(s):

- [LinkedIn endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/linkedin-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON returned by the Crawlora API, with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and supports documented LinkedIn company, product, showcase, product category, and product search routes.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
