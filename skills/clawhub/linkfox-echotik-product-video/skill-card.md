## Description: <br>
Queries promotional TikTok Shop videos associated with a product and summarizes engagement, estimated sales, GMV, creator, and publishing metadata for product video marketing analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, e-commerce analysts, and commerce-focused agents use this skill to inspect TikTok Shop product videos, compare engagement and estimated sales metrics, and identify influencer content that may be driving product performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API-authenticated product-video queries and possible feedback content are sent to LinkFox services. <br>
Mitigation: Install and use the skill only when that data sharing is acceptable, and avoid including sensitive business context in query or feedback content. <br>
Risk: Setting LINKFOX_TOOL_GATEWAY can redirect credentialed requests to an alternate endpoint. <br>
Mitigation: Leave LINKFOX_TOOL_GATEWAY unset unless the alternate endpoint is deliberately configured and trusted. <br>
Risk: Full API responses are persisted under linkfox/ and cached locally, which may expose sensitive product or market data in workspace files. <br>
Mitigation: Review and remove saved JSON files after use when needed, and avoid --inline or raw JSON output for sensitive datasets. <br>
Risk: Repeated lookups consume LinkFox credits. <br>
Mitigation: Warn users before repeated calls with new parameters and rely on the built-in 24-hour cache for identical requests. <br>


## Reference(s): <br>
- [EchoTik-TikTok商品视频 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-product-video) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, files, markdown] <br>
**Output Format:** [Markdown guidance with Python command examples; script output is saved JSON plus either full JSON or a compact text summary on stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a productId; supports sorting, time range, influencer filtering, pagination, 24-hour local caching, and optional inline full JSON output.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
