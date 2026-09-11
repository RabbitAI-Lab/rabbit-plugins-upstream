## Description:

Fetches live Amazon marketplace data through Apiguru for product details, prices, reviews, keyword search, best-sellers, deals, offers, stock, and seller profiles across 20 Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user requests current Amazon product, seller, pricing, stock, review, deal, or marketplace search data. It is scoped to Amazon marketplace data and includes consent guidance for any billable Apiguru calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable API calls may occur after the free quota or when using a keyed Apiguru account.

Mitigation: Run capabilities first, ask the user before billable calls or batches, agree on a spending cap, and stop on 402 responses.

Risk: An Apiguru API key could be exposed if handled casually.

Mitigation: Accept keys only through the reviewed prompt, stdin, or user-named key-file paths; do not echo keys or pass them on the command line.

Risk: The optional local MCP package path is separate from the reviewed skill artifact.

Mitigation: Prefer the included probe.py or hosted MCP endpoint; independently review, pin, and verify any local MCP package before use.

Risk: The feedback command posts user-provided text to a public feedback wall.

Mitigation: Post feedback only when the user explicitly asks and ensure the message contains no secrets or private data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Project Homepage](https://github.com/apiguru-app/agent-kit)
- [Endpoint Reference](references/endpoints.md)
- [Costs, Billing, and Retries](references/errors-and-costs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data commands; optional feedback command posts user-provided text publicly.]

## Skill Version(s):

1.1.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
