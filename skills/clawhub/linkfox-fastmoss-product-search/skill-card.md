## Description: <br>
Searches and filters TikTok Shop product data using FastMoss, including keyword search, market and category filters, commission ranges, sales metrics, creator counts, and sorting across 15 supported markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and e-commerce operators use this skill to search TikTok Shop products, compare sales and GMV metrics, identify commission opportunities, and inspect influencer-driven product performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and can make paid external product-search requests. <br>
Mitigation: Use a scoped API key where possible, control the relevant environment variables, and confirm cost-sensitive searches before repeated calls. <br>
Risk: Full API responses are retained locally and may contain product, shop, or query details from the user's task. <br>
Mitigation: Run the skill only in workspaces where local output paths are acceptable, review saved files, and remove retained responses when they are no longer needed. <br>
Risk: Feedback behavior can send user sentiment or issue details to a separate LinkFox feedback endpoint. <br>
Mitigation: Avoid sending sensitive feedback content and disable or review feedback-related use in sensitive workspaces. <br>
Risk: Onboarding instructions may prompt installation of a related LinkFox onboarding skill when authentication or credits fail. <br>
Mitigation: Review any additional skill before installation and require explicit user approval before downloading or installing related materials. <br>


## Reference(s): <br>
- [FastMoss-TikTok商品搜索 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-search) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>
- [LinkFox API Key Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables, shell commands, and JSON API results saved to local files or printed to stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are retained locally; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
