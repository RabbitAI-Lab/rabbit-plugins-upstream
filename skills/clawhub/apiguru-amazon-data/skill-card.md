## Description:

Provides live Amazon marketplace data from Apiguru for product details, prices, reviews, keyword search, best-sellers, deals, offers, stock, and seller profiles across supported Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve structured Amazon marketplace data by ASIN, Amazon URL, seller, product, or keyword, including price, stock, review, and monitoring workflows. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable Apiguru API calls may spend the user's account balance after the free/keyless allowance is exhausted.

Mitigation: Use the free/keyless path when possible, run capabilities before planning paid work, ask for explicit approval before billable calls, and agree on a task spending cap.

Risk: API keys can be exposed if placed in command arguments, logs, or unintended files.

Mitigation: Accept keys only through the documented prompt, standard input, or a user-named file; never echo keys, and rely on the reviewed script's fixed hosts and redirect refusal.

Risk: Feedback submitted through the feedback command or wall may become public.

Mitigation: Do not include secrets, private details, or sensitive customer data in feedback messages.

Risk: The optional MCP server is a separate component outside the packaged skill artifact.

Mitigation: Prefer the included probe script or hosted endpoint unless the MCP server has been separately reviewed, pinned, and deployed with least privilege.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apiguru-app/skills/apiguru-amazon-data)
- [Apiguru agent kit homepage](https://github.com/apiguru-app/agent-kit)
- [Endpoint reference](references/endpoints.md)
- [Costs, billing and retries](references/errors-and-costs.md)
- [Apiguru x402 endpoint metadata](https://agent.apiguru.app/.well-known/x402)
- [Apiguru LLM access notes](https://agent.apiguru.app/llms.txt)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List responses can be large; the skill documents limit, compact, and fields parameters to reduce response size.]

## Skill Version(s):

1.1.29 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
