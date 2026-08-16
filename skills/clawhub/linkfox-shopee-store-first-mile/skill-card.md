## Description:

Helps agents use Shopee Open Platform FirstMile workflows through LinkFox to manage first-mile tracking numbers, waybills, channels, transit warehouses, and bind or unbind actions for authorized Shopee stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border e-commerce operators and developers use this skill to inspect and operate Shopee FirstMile logistics for authorized stores, including generating tracking numbers, binding or unbinding orders, retrieving waybills, and checking channels or warehouses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle LinkFox account setup, API keys, and billing or payment order creation.

Mitigation: Use a dedicated API key and manually verify any payment, recharge, or account setup action before proceeding.

Risk: FirstMile bind and unbind operations can change logistics state for Shopee orders.

Mitigation: Confirm the intended store, order, and tracking details before executing generate, bind, or unbind actions.

Risk: Full API responses may be saved locally and can include sensitive order or tracking data.

Mitigation: Run the skill in a trusted workspace, restrict access to saved response files, and clean retained data when it is no longer needed.

## Reference(s):

- [Skill API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee FirstMile API index](https://open.shopee.com/documents/v2/v2.first_mile.get_unbind_order_list?module=96&type=1)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-first-mile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files, API calls, Guidance]

**Output Format:** [Markdown guidance with Python command examples, JSON API responses, and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may be printed inline for small results or summarized after the full response is saved locally.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
