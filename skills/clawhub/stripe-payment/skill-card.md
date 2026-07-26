## Description: <br>
Integrates with Stripe so an AI assistant can manage customers, payment intents, subscriptions, invoices, refunds, balances, and webhook verification through the Stripe REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to perform Stripe account workflows from an assistant, including customer setup, one-time payments, recurring subscriptions, invoice lookups, refunds, balance checks, and webhook verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate live Stripe charges, captures, refunds, subscription changes, and customer mutations when connected to production credentials. <br>
Mitigation: Use Stripe test keys by default, prefer tightly scoped restricted keys for production, and require explicit confirmation before every live financial or customer-mutating action. <br>
Risk: Payment client secrets or secret API keys could be exposed in assistant responses or logs. <br>
Mitigation: Do not display secret API keys or client_secret values in general chat logs, and route client_secret values only to the intended frontend payment flow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gaolfun/skills/stripe-payment) <br>
- [Stripe API documentation](https://stripe.com/docs/api) <br>
- [Stripe test cards](https://stripe.com/docs/testing#cards) <br>
- [Stripe CLI documentation](https://stripe.com/docs/stripe-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, API examples, SDK snippets, and structured status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Stripe object identifiers, transaction status, balances, invoice metadata, refund details, and setup guidance; client_secret values should be handled carefully and not exposed in general chat logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
