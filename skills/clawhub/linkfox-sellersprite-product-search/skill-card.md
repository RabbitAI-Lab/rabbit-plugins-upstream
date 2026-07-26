## Description: <br>
Searches and filters SellerSprite Amazon product data across supported marketplaces by keyword, category, price, sales, BSR, ratings, margins, fulfillment, seller, and brand criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce analysts use this skill to find, filter, and compare product opportunities using SellerSprite product-level data. It supports product research workflows such as sales filtering, BSR analysis, margin screening, seasonal comparisons, and competitor landscape review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product queries and full API results may be shared with LinkFox/SellerSprite and saved locally. <br>
Mitigation: Use the skill only for product research data that can be sent to the service, and manage or delete saved LinkFox data and cache files in shared workspaces. <br>
Risk: Calls consume credits, and repeated searches can create unexpected cost. <br>
Mitigation: Confirm billable calls with the user before running additional searches, changing keywords, or paginating through more results. <br>
Risk: The skill can report feedback externally when it detects praise, dissatisfaction, mismatch, or improvement opportunities. <br>
Mitigation: Ask for confirmation before submitting feedback and avoid including sensitive product-research details in feedback payloads. <br>


## Reference(s): <br>
- [SellerSprite Product Search API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-product-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under LinkFox session data; small responses may print inline, while large responses print summaries unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
