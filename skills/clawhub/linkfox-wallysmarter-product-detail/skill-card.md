## Description: <br>
Queries WallySmarter for single Walmart product details, including current attributes, price history, and sales trend data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, ecommerce operators, and product researchers use this skill to inspect one Walmart ItemId at a time, summarize product attributes, and review available price and sales trend history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and may make billable WallySmarter requests. <br>
Mitigation: Use only authorized LinkFox credentials and confirm credit consumption before calls, especially when historical stats are included. <br>
Risk: The skill stores full lookup responses and cache data locally. <br>
Mitigation: Review local retention behavior and clean saved LinkFox data or cache files when product research details should not persist. <br>
Risk: The skill can send automatic operational feedback to LinkFox. <br>
Mitigation: Review the feedback behavior before use and avoid sending sensitive product research details in feedback content. <br>
Risk: Setting LINKFOX_TOOL_GATEWAY to an untrusted host could redirect API traffic. <br>
Mitigation: Use the default gateway or a gateway host you explicitly trust. <br>


## Reference(s): <br>
- [WallySmarter-商品详情 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-wallysmarter-product-detail) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown summaries with JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Walmart ItemId and optional includeStats boolean; full responses may be cached and retained locally.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
