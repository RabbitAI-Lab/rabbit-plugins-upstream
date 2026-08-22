## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to retrieve public LinkedIn company, product, and showcase page data by known LinkedIn IDs for company profiling, product-page checks, and firmographic enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can send the API key to Crawlora paths beyond the documented LinkedIn company, product, and showcase endpoints.

Mitigation: Constrain use to GET /linkedin/company/{id}, /linkedin/product/{id}, and /linkedin/showcase/{id}; review commands before running them with a real CRAWLORA_API_KEY.

Risk: Requests require a Crawlora API key, which could expose account access if mishandled.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid placing it in URLs or committed files, and rotate it if it is exposed.

## Reference(s):

- [linkedin-research endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/linkedin-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests and returns public LinkedIn company, product, or showcase page data.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
