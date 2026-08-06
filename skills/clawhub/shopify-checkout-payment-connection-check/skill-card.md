## Description: <br>
Safely inspect a Shopify store's cart-to-checkout path, destination-specific delivery choices, visible payment methods, payment setup, and aggregated payment signals without placing an order, submitting payment details, or changing store data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchants, ecommerce operators, and developers use this skill to check whether shoppers can reach checkout, see delivery choices, and reach visible payment options using merchant-authorized read-only Shopify evidence and a safe storefront walkthrough. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use against a Shopify store without merchant authorization could expose store checkout, delivery, or payment information. <br>
Mitigation: Install and run the skill only for stores where the merchant has authorized access, and use the documented read-only Shopify scopes. <br>
Risk: Local configuration and diagnostic files can contain sensitive store or credential-adjacent information. <br>
Mitigation: Keep skill-hub.env, client credentials, automation tokens, and checkout-admin.json private and outside the skill source. <br>
Risk: Visible payment methods or aggregate transaction errors can be misread as proof that payments fully work or that one provider caused all failures. <br>
Mitigation: Report checkout observations, Admin evidence, unknowns, and limitations separately, and state that a completed payment was not tested. <br>
Risk: A storefront walkthrough can create a temporary unsubmitted checkout session. <br>
Mitigation: Use only synthetic shopper data, stop before payment confirmation, and never place an order or enter payment credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-checkout-payment-connection-check) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [Connect Your Store](references/onboarding-guide.md) <br>
- [API surfaces and interpretation](references/api-surfaces.md) <br>
- [ShopifyPaymentsAccount](https://shopify.dev/docs/api/admin-graphql/2026-07/objects/ShopifyPaymentsAccount) <br>
- [OrderTransaction](https://shopify.dev/docs/api/admin-graphql/2026-07/objects/OrderTransaction) <br>
- [deliveryProfiles](https://shopify.dev/docs/api/admin-graphql/2026-07/queries/deliveryProfiles) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown or plain-language text with shell command examples and local JSON diagnostic output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only aggregate checkout, delivery, payment setup, and transaction-signal evidence; local outputs may include checkout-admin.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
