## Description: <br>
Fetches product-level metrics for a specific Ozon shop or seller from Seerfar, including 30-day sales, price, rating, weight, fulfillment, seller type, return or cancellation rate, and shop-level 30-day sales. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and e-commerce analysts use this skill to inspect a known Ozon seller's catalog, rank products by sales, price, rating, or listing time, and prepare competitor-shop product analysis from Seerfar data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A custom LINKFOX_TOOL_GATEWAY can receive the API key used by the skill. <br>
Mitigation: Avoid setting LINKFOX_TOOL_GATEWAY unless the destination is controlled and trusted. <br>
Risk: Full Ozon analytics responses may be persisted in the workspace or session data directory. <br>
Mitigation: Use the skill only in workspaces where saving those responses is acceptable, and review saved files before sharing or committing workspace contents. <br>
Risk: Authentication or quota recovery can involve an external onboarding-skill download. <br>
Mitigation: Confirm the onboarding download before allowing installation, and prefer existing onboarding guidance when available. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-shop-search) <br>
- [Seerfar Ozon 店铺商品搜索 API 参考](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, code, guidance] <br>
**Output Format:** [Markdown tables and summaries, JSON API responses, and Python or curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may be saved as JSON under a linkfox session data directory; the API uses paginated requests with a maximum pageSize of 20 and consumes LinkFox credits.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
