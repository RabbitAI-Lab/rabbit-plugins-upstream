## Description:

Browses Wayfair's category taxonomy and retrieves category product grids and product details including price, brand, stock status, ratings, variants, and images through the Crawlora API, returning normalized JSON for agent analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Wayfair categories, inspect category product grids, and retrieve product detail JSON for pricing, availability, rating, variant, and image comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key can be sent to an overridden API base rather than the intended Crawlora endpoint.

Mitigation: Use a trusted execution environment, keep the key in CRAWLORA_API_KEY only, and unset or validate CRAWLORA_API_BASE before use.

Risk: The bundled helper accepts broader paths and methods than the stated Wayfair-only workflow.

Mitigation: Restrict agent calls to the documented Wayfair GET endpoints and review proposed commands before execution.

Risk: Wayfair category labels are derived from URL slugs and may be imperfect.

Mitigation: Treat category names as best-effort discovery labels and verify important product decisions against returned product details.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/wayfair-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and limited to Wayfair categories, category grids, and product detail.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
