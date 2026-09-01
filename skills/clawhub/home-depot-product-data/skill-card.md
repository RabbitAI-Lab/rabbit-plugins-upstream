## Description:

Search Home Depot, pull full item detail and page through review bodies as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to search Home Depot products, retrieve item details, collect review pages, monitor retail pricing, and enrich product catalogs through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home Depot lookup requests are sent to Scavio and consume Scavio credits.

Mitigation: Keep the API key in an environment variable or secret store, and set a page or spend limit before broad searches or review collection.

Risk: Invalid sort values, broad pagination, or review pages past total_pages can produce billed empty results or errors.

Mitigation: Use only documented sort_by values, avoid custom page sizes, cap search and review loops, and stop reviews at total_pages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/home-depot-product-data)
- [Scavio Home Depot Search API Documentation](https://scavio.dev/docs/home-depot-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands, code snippets, and structured JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Home Depot endpoints consume Scavio credits and have fixed pagination limits.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
