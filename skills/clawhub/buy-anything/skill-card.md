## Description: <br>
Purchase products from Amazon and Shopify stores through conversational checkout when a user provides a supported product link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsyvic](https://clawhub.ai/user/tsyvic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to buy products from supported Amazon and Shopify product pages through a conversational checkout flow. The agent collects shipping details, a payment token, a spending limit, and same-turn confirmation before submitting an order. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real online orders and spend money. <br>
Mitigation: Use a spending limit, review the item and total before confirming, and require a fresh same-turn yes before each purchase. <br>
Risk: Saving a BasisTheory token, address, and spending limit in agent memory may increase exposure if the host memory is accessible or retained unexpectedly. <br>
Mitigation: Save checkout data only with explicit user permission, use a fresh token instead of saving one when risk is unacceptable, and delete saved memory when it is no longer needed. <br>
Risk: Unsupported product URLs, checkout failures, or CVC refresh requirements can interrupt purchase completion. <br>
Mitigation: Limit use to Amazon and Shopify product URLs, surface Rye failure messages to the user, and retry only after the user completes any required CVC refresh and confirms. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/tsyvic/skills/buy-anything) <br>
- [Rye API documentation](https://docs.rye.com) <br>
- [BasisTheory](https://basistheory.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash curl commands and order-status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, a supported Amazon or Shopify product URL, shipping details, a BasisTheory token, a spending limit, and same-turn purchase confirmation.] <br>

## Skill Version(s): <br>
3.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
