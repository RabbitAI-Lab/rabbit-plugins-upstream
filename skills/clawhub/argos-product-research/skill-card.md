## Description: <br>
Search, compare, and research products from Argos.co.uk with natural language queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[notsurewhoisthis](https://clawhub.ai/user/notsurewhoisthis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to find Argos products, compare options, inspect pricing and availability, and summarize customer review themes before making purchasing decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product searches and detail lookups may send user queries to Argos or web search. <br>
Mitigation: Avoid including sensitive personal data in product queries and prefer public product identifiers or generic search terms. <br>
Risk: Prices, stock, delivery options, and reviews can change after the agent fetches them. <br>
Mitigation: Verify current purchase-critical details directly on Argos before buying. <br>
Risk: Optional caching can store product data locally when enabled. <br>
Mitigation: Leave caching disabled unless needed, and use a short cache TTL for time-sensitive product data. <br>


## Reference(s): <br>
- [Argos](https://www.argos.co.uk) <br>
- [Argos Product Research on ClawHub](https://clawhub.ai/notsurewhoisthis/skills/argos-product-research) <br>
- [Publisher Profile](https://clawhub.ai/user/notsurewhoisthis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown tables and concise prose with product links, comparisons, review summaries, and recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include current prices, availability, delivery options, ratings, review themes, and optional locally cached product data when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
