## Description:

Helps agents manage Temu US product pricing through LinkFox-mediated Partner US APIs for price-order queries, SKU base-price changes, recommended prices, and base-price estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, operators, and developers use this skill to query Temu US pricing records, estimate or retrieve recommended supplier prices, and submit SKU base-price changes through LinkFox gateway scripts.

### Deployment Geography for Use:

United States (Temu US site)

## Known Risks and Mitigations:

Risk: The security scan flags broader credential, proxy, file-download, response-storage, onboarding, and payment-order capabilities than a narrow US pricing skill needs.

Mitigation: Install only when LinkFox-mediated Temu operations are required, and run it in a dedicated workspace.

Risk: The skill can use and persist LinkFox and Temu credentials, including a plaintext local Temu token store.

Mitigation: Keep LINKFOX_* gateway variables pointed only at trusted LinkFox hosts, avoid passing real tokens on command lines, and protect or relocate the token store.

Risk: Onboarding and payment-order commands can affect accounts or billing.

Mitigation: Treat onboarding or payment-order commands as explicit account and billing actions that require user confirmation.

Risk: Saved response files may contain business, pricing, or account data.

Mitigation: Delete saved response files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-us)
- [linkfox-temu-price-us API reference](references/api.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Partner US price interface catalog](references/partner-us-catalog.md)
- [Price API documentation index](references/apis/README.md)
- [Price-order query API](references/apis/bg-local-goods-priceorder-query.md)
- [Change SKU base-price API](references/apis/bg-local-goods-priceorder-change-sku-price.md)
- [Base-price recommendation API](references/apis/temu-local-goods-baseprice-recommend.md)
- [Recommended-price query API](references/apis/temu-local-goods-recommendedprice-query.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI scripts print JSON summaries and save full JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under a LinkFox session data directory; small responses may also be printed inline.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
