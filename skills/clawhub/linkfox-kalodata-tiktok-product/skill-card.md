## Description: <br>
Uses LinkFox/Kalodata endpoints to help agents browse TikTok Shop product leaderboards and retrieve detailed product metrics by product ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents researching TikTok Shop products use this skill to find ranked or best-selling products, then inspect detailed price, sales, revenue, commission, category, shop, video, live, and creator metrics for a selected product. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authorization and session metadata are sent to the configured LinkFox gateway, and the gateway host can be overridden. <br>
Mitigation: Use the default gateway or set LINKFOX_TOOL_GATEWAY only to an endpoint you trust to receive authorization and session metadata. <br>
Risk: Full product-query responses are saved locally, which can expose commercial research data in the workspace. <br>
Mitigation: Run the skill only in a workspace where persisted product-query results are acceptable, and review or clean saved LinkFox output files when the task is complete. <br>
Risk: API calls consume credits, and some valid but empty requests may still be billed. <br>
Mitigation: Confirm region, date range, page size, and productId before calling; avoid repeated probing unless the user accepts the additional cost. <br>
Risk: The artifact includes a separate feedback endpoint that may send user feedback outside the product data gateway. <br>
Mitigation: Review feedback behavior before installation and avoid sending sensitive user or business details in feedback content. <br>


## Reference(s): <br>
- [Kalodata-TikTok商品搜索与详情 API 参考](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-product) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses, saved JSON files, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Product ranking responses are paginated and detail lookup requires a productId; scripts save full responses locally and may print either full JSON or a summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
