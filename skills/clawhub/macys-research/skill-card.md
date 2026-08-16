## Description:

Looks up a Macy's product's full detail and customer reviews by its numeric productId, and pulls Macy's own search-box typeahead suggestions using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to retrieve public Macy's product details, customer review summaries, and Macy's typeahead suggestions when they already have a numeric productId or a partial suggestion query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths, which may use the configured API key beyond the Macy's endpoints described by the skill.

Mitigation: Restrict agent use to the three documented Macy's GET endpoints or replace the helper with a narrower wrapper before deployment.

Risk: The skill requires a Crawlora API key that could be exposed or misused if included in prompts, files, URLs, or logs.

Mitigation: Provide the key only through the CRAWLORA_API_KEY environment variable and review agent traces for accidental credential disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/macys-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key and either a known Macy's numeric productId or a typeahead query.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
