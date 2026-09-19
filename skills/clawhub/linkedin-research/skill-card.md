## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON for public company-related LinkedIn research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enrich company, competitor, product, or showcase-page research with public LinkedIn data when they already have the relevant LinkedIn ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the requested LinkedIn company, product, or showcase IDs and authenticates calls with the user's Crawlora API key.

Mitigation: Use only with approved public company-related LinkedIn data, keep CRAWLORA_API_KEY in the environment, and do not hardcode or commit the key.

Risk: The skill does not support personal LinkedIn profiles, LinkedIn login access, private content, or ID discovery.

Mitigation: Decline or redirect requests for personal profiles, private LinkedIn data, login-based access, or search/discovery outside the documented company/product/showcase ID endpoints.

Risk: Requests outside the documented Crawlora LinkedIn route set could broaden the data surface or expose credentials to unintended destinations.

Mitigation: Use the bundled helper route catalog for calls and keep the API base fixed to Crawlora's documented API host.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/linkedin-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a LinkedIn company, product, or showcase page ID; public company-related pages only.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
