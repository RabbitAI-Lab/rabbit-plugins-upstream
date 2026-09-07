## Description:

Researches Zappos footwear and apparel catalog data through the Crawlora API, including brand listings, product search, pricing, images, ratings, fit feedback, and color variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up public Zappos brand, search, suggestion, and product-detail data without scraping HTML. It supports catalog research, product comparison, pricing checks, and fit-feedback summaries for footwear and apparel questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and unsafe invocation can expose credentials.

Mitigation: Keep the key only in CRAWLORA_API_KEY, do not place it in URLs or committed files, and supervise generated commands before execution.

Risk: The helper script is broader than the Zappos-only use case.

Mitigation: Allowlist only the documented /zappos routes and remove unrelated endpoint examples before deployment.

Risk: Unsafe parameters or environment settings can make curl read local files or send requests to an unintended API base.

Mitigation: Require literal name=value query parameters and use the documented Crawlora API base unless an operator has explicitly approved a different endpoint.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Zappos brand, search, and product results are paginated.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
