## Description:

Provides agent guidance and Python helpers for managing Temu US products through LinkFox, including product queries, edits, deletion, stock, sale status, compliance, external IDs, and video cover lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to guide agent-assisted Temu US product-management API calls through LinkFox. It helps choose the correct Manage Product endpoint, parameters, authentication path, and local response handling for Temu US catalog operations.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can support real Temu store-management actions, including delete, full update, stock, sale-status, pre-sale, billing, and credential-related workflows.

Mitigation: Require operator confirmation of the exact store, site, goodsId, SKU, and requested action before executing destructive or business-impacting operations.

Risk: The skill handles LinkFox and Temu tokens and can save Temu access tokens locally.

Mitigation: Use only on trusted machines, avoid pasting long-lived tokens into shared prompts or logs, and protect or relocate the local token store.

Risk: Saved response archives may contain sensitive store, product, or operational data.

Mitigation: Periodically review and delete saved LinkFox response archives when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-us)
- [API reference](references/api.md)
- [Partner US catalog](references/partner-us-catalog.md)
- [Access token guide](references/access-token.md)
- [Temu Partner US Manage Product documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2a343c65a03d42d380e9ad835aa7b54b)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples and Python command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses under the current working directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
