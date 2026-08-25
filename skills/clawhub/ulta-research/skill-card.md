## Description:

Researches Ulta Beauty's catalog - categories, products, shades, questions, reviews, and nearby stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to search and browse Ulta Beauty products, inspect product details, shades, questions, reviews, and locate nearby stores through Crawlora instead of scraping Ulta directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ulta-related searches, product IDs, and optional store-location inputs are sent to Crawlora.

Mitigation: Use the skill only when that disclosure is acceptable, and avoid entering sensitive or unnecessary location details.

Risk: The Crawlora API key could be exposed if hardcoded, logged, or committed.

Mitigation: Keep the key in CRAWLORA_API_KEY and avoid storing it in source files, command history snippets, logs, or shared outputs.

Risk: The helper can call non-Ulta Crawlora API paths if invoked with other endpoints.

Mitigation: Restrict routine use to the documented /ulta endpoints unless broader Crawlora API access is intentional.

## Reference(s):

- [Ulta endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ulta-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; listing, question, and review endpoints are paginated.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
