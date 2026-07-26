## Description: <br>
Accept payments on a Polsia-built site via Stripe Connect payment links, then verify them server-side without the Stripe SDK, webhooks, or STRIPE_SECRET_KEY. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentlevier](https://clawhub.ai/user/agentlevier) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to add Polsia-hosted Stripe Connect payments, create payment links, poll for completed checkout sessions, and verify fulfillment server-side. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment links can fail or redirect incorrectly when success_url is omitted or hardcoded Stripe links are used. <br>
Mitigation: Always create links through the Polsia payment-link tools and pass an application success_url containing the checkout session placeholder. <br>
Risk: Fulfillment can run before Polsia records the Stripe webhook result or can run more than once. <br>
Mitigation: Poll the server-side verification endpoint after redirect and make fulfillment idempotent using the checkout session ID. <br>
Risk: Secrets or wrong API endpoints can expose credentials or send payment verification to the wrong service. <br>
Mitigation: Use POLSIA_API_KEY only on the server, use POLSIA_API_BASE_URL for payment endpoints, and do not add STRIPE_SECRET_KEY, the Stripe SDK, or webhooks. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/agentlevier/skills/polsia-stripe-payments) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown guidance with code and endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational constraints for Stripe Connect onboarding, success URL handling, polling, server-side verification, and idempotent fulfillment.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
