## Description: <br>
Pricing Strategy helps agents guide pricing decisions by auditing customer value, willingness to pay, anchors, tier structure, loss-aversion framing, stress tests, and 60-day measurement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business operators use this skill when setting an initial price, planning a price change, designing freemium, tiered, usage-based, or outcome-based pricing, or evaluating whether pricing is anchored to customer value rather than cost or competitors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence customer-facing pricing decisions with revenue, churn, or market-positioning impact. <br>
Mitigation: Treat outputs as advisory and require human review before changing real prices, discounts, tiers, or customer communications. <br>
Risk: Examples involving AI inference costs may become stale as model capabilities and API prices change. <br>
Mitigation: Verify current market, competitor, and API pricing before quoting figures or setting production prices. <br>


## Reference(s): <br>
- [Primary Pricing Sources](references/sources.md) <br>
- [De Beers and the Engagement Ring](examples/de-beers-and-the-engagement-ring-1947-ongoing.md) <br>
- [Netflix Qwikster Price Restructuring](examples/netflix-qwikster-price-restructuring-2011.md) <br>
- [Pricing an AI Product Under Volatile Inference Costs](examples/ai-product-pricing-under-volatile-inference-costs-2023-2026.md) <br>
- [Pricing Strategy on ClawHub](https://clawhub.ai/deciqai/skills/pricing-strategy) <br>
- [Prospect Theory](https://www.jstor.org/stable/1914185) <br>
- [Toward a Positive Theory of Consumer Choice](https://doi.org/10.1016/0167-2681(80)90051-7) <br>
- [Have You Ever Tried to Sell a Diamond?](https://www.theatlantic.com/magazine/archive/1982/02/have-you-ever-tried-to-sell-a-diamond/304575/) <br>
- [OpenAI API Pricing](https://openai.com/api/pricing/) <br>
- [Anthropic Pricing](https://www.anthropic.com/pricing) <br>
- [Google AI Pricing](https://ai.google.dev/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown coaching response with a filled Pricing Audit table when enough user input is available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause at explicit WAIT points to collect user input before continuing the pricing audit.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
