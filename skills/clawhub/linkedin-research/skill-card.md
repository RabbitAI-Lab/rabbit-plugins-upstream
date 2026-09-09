## Description:

Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to retrieve public LinkedIn company, product, and showcase page data by known LinkedIn IDs for company profiling, product audits, and firmographic enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call non-LinkedIn Crawlora endpoints and send POST bodies, which is broader than the advertised LinkedIn-only scope.

Mitigation: Restrict usage to the documented LinkedIn company, product, and showcase GET endpoints, and review command paths before execution.

Risk: Setting CRAWLORA_API_BASE can redirect authenticated requests and expose the Crawlora API key to an unintended host.

Mitigation: Avoid setting CRAWLORA_API_BASE; use a low-privilege Crawlora API key and prefer a release that hardcodes or validates the Crawlora API origin.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill page](https://clawhub.ai/tonywangcn/skills/linkedin-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON API output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides authenticated Crawlora API calls and expects public LinkedIn company, product, or showcase IDs supplied by the user or an upstream source.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
