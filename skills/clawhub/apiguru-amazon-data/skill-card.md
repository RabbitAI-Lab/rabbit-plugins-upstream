## Description:

Apiguru Amazon Data helps agents fetch live Amazon marketplace product, pricing, review, offer, stock, seller, keyword search, best-seller, and deals data from Apiguru across 20 Amazon marketplaces, with explicit consent required before billable calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user asks for live Amazon data by ASIN, Amazon URL, product, seller, or keyword, or for Amazon price, stock, and review monitoring. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable API calls may spend the user's Apiguru account balance or paid quota.

Mitigation: Before the first billable call, batch, or broad search, state the planned calls, item count, and expected cost, get explicit approval, set a task cost cap, and stop on payment-required responses.

Risk: API keys or private data could be exposed if credentials are searched for, echoed, or passed through unsafe channels.

Mitigation: Use only credentials the user deliberately provides through the reviewed script's prompt, stdin, or a user-named file, never echo keys, and send keys only to the Apiguru keyed API host.

Risk: The optional MCP package has separate supply-chain and runtime risk outside the reviewed script path.

Mitigation: Prefer the bundled script or hosted MCP endpoint; if a local MCP package is required, pin the version, verify the artifact, and run it with limited filesystem, credential, and network access.

Risk: The feedback command posts submitted text to a public wall.

Mitigation: Do not include secrets, personal data, or private conversation text in feedback messages.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Project homepage](https://github.com/apiguru-app/agent-kit)
- [Apiguru endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru x402 capabilities](https://agent.apiguru.app/.well-known/x402)
- [Apiguru payment documentation](https://agent.apiguru.app/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live paid API results; billable calls require explicit user consent and an agreed cost cap.]

## Skill Version(s):

1.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
