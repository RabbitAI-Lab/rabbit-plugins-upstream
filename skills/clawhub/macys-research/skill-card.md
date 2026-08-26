## Description:

Looks up a Macy's product's full detail and customer reviews by its numeric productId, and pulls Macy's own search-box typeahead suggestions using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to retrieve public Macy's product details, customer review summaries, paginated reviews, and typeahead suggestions when they already have a numeric Macy's productId or a partial query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send requests to Crawlora API paths and methods beyond the Macy's endpoints described by the skill.

Mitigation: Restrict agent use to the documented Macy's endpoints, review commands before execution, and avoid exposing the helper where unrestricted Crawlora API access is not acceptable.

Risk: The skill requires a reusable Crawlora API key.

Mitigation: Provide the key through CRAWLORA_API_KEY only, rotate it if exposed, and do not place it in prompts, command arguments, source files, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/macys-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known Macy's productId for product detail and review lookups.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
