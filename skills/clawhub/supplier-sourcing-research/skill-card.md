## Description:

Discover and compare suppliers behind brands using Crawlora's ImportYeti company reports and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sourcing teams, and developers use this skill to build supplier shortlists from observed ImportYeti shipment evidence, public company pages, and follow-up qualification questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API script can expose the Crawlora API key to an overridden API base URL.

Mitigation: Leave CRAWLORA_API_BASE unset for normal use, or set it only to a fully trusted endpoint.

Risk: Supplier-research queries and selected public-website extraction requests are sent to Crawlora with the user's API key.

Mitigation: Do not include secrets, private files, or confidential business data in request bodies or query parameters.

Risk: Shipment records and extracted public-page data can be incomplete or ambiguous.

Mitigation: Link claims to source reports or pages, preserve ambiguous dates and unavailable fields, and treat shipment records as observations rather than proof of manufacturing quality or capacity.

## Reference(s):

- [supplier-sourcing-research endpoint reference](reference/endpoints.md)
- [ImportYeti coverage notes](https://www.importyeti.com/our-data)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/supplier-sourcing-research)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown with inline shell commands and source-linked supplier shortlist fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include supplier names, countries or addresses, observed customer relationships, shipment metric and date scope, official websites, fit rationale, and open qualification questions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
