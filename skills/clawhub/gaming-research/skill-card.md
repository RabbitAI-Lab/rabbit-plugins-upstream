## Description:

Researches video games through the Crawlora API for Steam and PlayStation Store listings, prices, reviews, player counts, charts, tags, achievements, categories, and deals, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and game researchers use this skill to look up game pricing, reviews, player counts, trending charts, sale listings, and store details across Steam and PlayStation Store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call non-gaming Crawlora endpoints with the user's API key, which may spend credits outside the intended gaming research use case.

Mitigation: Review commands before execution and restrict calls to the documented Steam and PlayStation endpoints unless broader Crawlora access is intentionally needed.

Risk: Requests require a Crawlora API key and can consume Crawlora credits.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, monitor credit use, and avoid committing or passing the key in URLs or prompts.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results depend on Crawlora API, Steam, and PlayStation Store data availability.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
