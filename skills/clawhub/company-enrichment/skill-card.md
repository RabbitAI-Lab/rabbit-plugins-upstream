## Description:

Company firmographics, tech stack, headcount, and intelligence from a domain — agent-ready account research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External sales and research teams use the skill to enrich company domains or names with firmographics and account intelligence. Agents can use the results to research accounts, build target lists, and filter companies against an ideal customer profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers and account lists are sent to the external Superagnt service, and requests can consume service credits.

Mitigation: Share only approved company data and check credit usage before running large or bulk requests.

Risk: The API key could be exposed or granted broader access than intended through optional MCP access.

Mitigation: Store the key securely rather than pasting it into chat, and inspect the enabled MCP tools and permissions before use.

Risk: Request examples and schemas in the skill documentation may need correction before use.

Mitigation: Check and correct the request examples against valid schemas before sending requests.

## Reference(s):

- [Company Enrichment documentation](https://superagnt.com/r/ch-company-enrichment-docs)
- [Company Enrichment listing](https://clawhub.ai/superagnt/skills/company-enrichment)
- [Company Enrichment MCP setup](https://www.superagnt.com/install?facet=company-enrichment)
- [Superagnt API key setup](https://superagnt.com/r/ch-company-enrichment-key)

## Skill Output:

**Output Type(s):** [Analysis, Structured company data]

**Output Format:** [JSON company research results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by selected company research operation.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
