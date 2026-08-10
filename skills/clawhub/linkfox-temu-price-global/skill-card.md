## Description:

Helps agents query and update Temu Global (non-US/EU) pricing and supplier-price APIs through the LinkFox gateway, covering price orders, recommended prices, SKU supplier-price lists, base-price recommendations, and batch SKU price changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators managing Temu Global seller pricing use this skill to run guided API calls for supplier-price lookup, recommended-price checks, price-order review, signed file download, and batch SKU price updates.

### Deployment Geography for Use:

Global, for Temu Global seller workflows excluding the US and EU site-specific skills.

## Known Risks and Mitigations:

Risk: The skill bundles broad Temu API proxying, file download, local token handling, payment onboarding, and live price-change capabilities.

Mitigation: Install only if these capabilities are needed, review the enabled scripts before use, and restrict operation to approved Temu stores and workflows.

Risk: Temu access tokens may be stored locally or emitted by token retrieval utilities.

Mitigation: Use least-privilege Temu tokens, keep token files private, avoid unmasked token listing or raw token output, and rotate tokens if exposed.

Risk: Batch SKU price changes can affect live seller pricing.

Mitigation: Require explicit user confirmation, verify store, site, goodsId, skuId, currency, and price payloads, and perform a post-change price-order query for confirmation.

Risk: Gateway and billing/onboarding flows can use configured LinkFox credentials and initiate paid actions.

Mitigation: Verify gateway environment variables and require explicit user confirmation before payment, order, or account onboarding actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-global)
- [API Reference](references/api.md)
- [Partner Global Price Catalog](references/partner-global-catalog.md)
- [Access Token Guide](references/access-token.md)
- [Temu Partner Global Documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request/response payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses as JSON files under a linkfox session directory and summarize large responses unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
