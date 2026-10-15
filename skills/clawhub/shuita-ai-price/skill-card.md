## Description:

Helps users compare AI subscription and account prices across marketplaces using Shuita price data and explains differences between product types and official pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gm365](https://clawhub.ai/user/gm365)

### License/Terms of Use:

MIT-0

## Use Case:

People comparing ChatGPT, Claude, Gemini, Grok, or Cursor subscriptions use this skill to check current marketplace price ranges, compare them with official rates, and understand differences between offers. It does not select sellers or make purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pricing and availability depend on Shuita data and may change before a purchase.

Mitigation: Check the quoted update time and confirm price, stock, offer terms, and seller support before buying.

Risk: The optional MCP installation command fetches the latest published package without pinning a version.

Mitigation: In sensitive environments, review the package and install a pinned version instead.

## Reference(s):

- [Shuita price comparison](https://shuita.xyz)
- [Shuita MCP integration](https://shuita.xyz/mcp)
- [Shuita current price listings](https://shuita.xyz/llms.txt)
- [Shuita monthly reports](https://shuita.xyz/reports)
- [AI subscription buying checklist](https://shuita.xyz/guide/ai-subscription-buying-checklist)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown price comparisons with source links and offer caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes price, product type, data update time, and a product link when quoting an offer.]

## Skill Version(s):

1.0.0 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
