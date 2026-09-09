## Description:

Researches Ulta Beauty's catalog -- categories, products, shades, questions, reviews, and nearby stores -- using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to search Ulta Beauty products, browse categories, inspect shades, summarize product questions and reviews, and find nearby Ulta stores through Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an overridden API destination.

Mitigation: Use the default Crawlora API base unless the alternate destination is fully trusted, and prefer a low-privilege or disposable Crawlora key.

Risk: Store searches may disclose sensitive location details.

Mitigation: Avoid sending sensitive personal details or precise locations when a broader city, region, or zip code is sufficient.

Risk: The helper script exposes broader Crawlora API behavior than the Ulta-focused skill description.

Mitigation: Review shell commands before execution and restrict use to the Ulta endpoints documented for this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ulta-research)
- [Ulta endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; API results are paginated for searches, categories, product questions, and product reviews.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
