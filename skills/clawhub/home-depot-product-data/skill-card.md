## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON. 3 endpoints for retail price monitoring, catalog enrichment and review mining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Home Depot products, retrieve product details, and page through customer review data for retail price monitoring, catalog enrichment, and review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries and item identifiers are sent to Scavio as a third-party API provider.

Mitigation: Avoid sending sensitive private text as search queries or item identifiers, and install only when third-party API use is acceptable.

Risk: Each Home Depot endpoint call spends API credits, including empty results and invalid paging or sort choices.

Mitigation: Set a page budget before looping, use only documented sort values, and stop review paging at the returned total_pages value.

Risk: The skill requires SCAVIO_API_KEY to make requests.

Mitigation: Load the key from the environment or a secret store and do not hard-code it in source files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/home-depot-product-data)
- [Scavio Home Depot Search Documentation](https://scavio.dev/docs/home-depot-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=home-depot-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=home-depot-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON API guidance, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured JSON from Scavio API endpoints when executed by an agent with SCAVIO_API_KEY.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
