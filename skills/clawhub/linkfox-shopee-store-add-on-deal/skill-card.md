## Description:

Manages Shopee Add-On Deal promotions for authorized stores using LinkFox scripts that call the Shopee Open API Add-On Deal module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and developers use this skill to create, query, update, delete, and end Shopee Add-On Deal promotions for authorized shops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live Shopee store promotions.

Mitigation: Confirm the target shop and deal IDs, then require explicit approval before create, update, delete, or end actions.

Risk: Authentication, billing, and payment flows may expose sensitive API keys or initiate payment/order actions.

Mitigation: Use only trusted LinkFox endpoint environment variables and require explicit approval before payment or order actions.

Risk: Printed API keys and saved linkfox response folders may contain sensitive store or account data.

Mitigation: Treat console output and saved response folders as sensitive and clean them up when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-add-on-deal)
- [Shopee Add-On Deal official API index](https://open.shopee.com/documents/v2/v2.add_on_deal.add_add_on_deal?module=111&type=1)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are printed when small, summarized when large, and saved under a linkfox response folder for later inspection.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
