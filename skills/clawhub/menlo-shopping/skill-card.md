## Description: <br>
Use Menlo Shopping MCP to find individual products or build curated shopping lists. Use when a user asks to shop, compare products, find gifts, assemble a setup, or get product recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[t-khush](https://clawhub.ai/user/t-khush) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use this skill to search Amazon.com products, compare options, find gifts, and assemble curated shopping lists based on user constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured Menlo Shopping MCP server may return product links, prices, ratings, or availability that need review before purchase decisions. <br>
Mitigation: Confirm you trust the configured MCP server and review returned product details, links, prices, ratings, and availability before spending money. <br>
Risk: Recommendation quality depends on user constraints and returned product data. <br>
Mitigation: Keep searches specific, apply user-provided price or rating constraints, and explain why each pick fits the request. <br>


## Reference(s): <br>
- [Menlo Shopping on ClawHub](https://clawhub.ai/t-khush/skills/menlo-shopping) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or text product recommendations with product links and concise rationale] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses returned prices, ratings, availability facts, and product URLs without inventing missing details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
