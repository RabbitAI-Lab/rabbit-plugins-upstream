## Description: <br>
Queries TikTok creator shop and showcase or live-bag products through LinkFox /tiktokVideo/developerProxy, returning product data and product_id values for shoppable-video precheck and publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commerce operators and agents use this skill to search TikTok creator-bound shop products or list showcase and live-bag products, then carry product_id values into LinkFox TikTok video precheck and publishing flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires trust in LinkFox with the configured API key and TikTok creator product data. <br>
Mitigation: Install only if LinkFox is trusted for this data; keep API keys in environment variables and do not expose full tokens or private account details. <br>
Risk: The skill may direct installation of a separate onboarding or authorization-related skill when setup or dependencies are missing. <br>
Mitigation: Review and explicitly approve any additional skill installation before allowing the agent to install or run it. <br>
Risk: Saved response files may contain TikTok creator product data or gateway responses. <br>
Mitigation: Store response files only in appropriate locations and delete them when they are no longer needed. <br>
Risk: The skill can submit feedback based on agent judgment. <br>
Mitigation: Review feedback content and avoid including tokens, private account data, or sensitive business details. <br>


## Reference(s): <br>
- [TikTok Video Products API Reference](references/api.md) <br>
- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-products) <br>
- [TikTok Shop Get Shop Products 202509](https://partner.tiktokshop.com/docv2/page/get-shop-products-202509) <br>
- [TikTok Shop Get Showcase Products 202405](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405) <br>
- [Shoppable Video Integration Solutions V2025.Q4.01](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist large API responses to local JSON files for later field extraction.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
