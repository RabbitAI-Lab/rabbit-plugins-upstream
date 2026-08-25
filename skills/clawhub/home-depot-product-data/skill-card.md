## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON. 3 endpoints for retail price monitoring, catalog enrichment and review mining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search Home Depot products, inspect structured item details, and page through customer reviews for price monitoring, catalog enrichment, and review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send Home Depot search terms, product identifiers, and review lookups to Scavio.

Mitigation: Avoid sending sensitive internal product lists or private research terms unless that data sharing is acceptable.

Risk: Each endpoint call consumes Scavio credits, including empty or invalid searches.

Mitigation: Set a page and credit budget before broad searches or review mining, and stop review paging at total_pages.

Risk: The API key can authorize paid or quota-limited requests if exposed.

Mitigation: Store SCAVIO_API_KEY in environment or secret storage and keep it out of source control and chat transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/home-depot-product-data)
- [Scavio Home Depot API documentation](https://scavio.dev/docs/home-depot-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance centers on structured JSON responses from Scavio's Home Depot search, product, and reviews endpoints.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
