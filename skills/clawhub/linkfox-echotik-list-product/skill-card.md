## Description: <br>
Searches and analyzes TikTok Shop product data, including sales, influencer-driven promotion data, pricing, and commission rates across 16 marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and e-commerce analysts use this skill to search TikTok Shop products, compare sales and GMV metrics, identify high-commission or influencer-promoted products, and decide whether to run additional paid EchoTik queries. <br>

### Deployment Geography for Use: <br>
Global, with product data queries limited to the supported TikTok Shop marketplaces: US, ID, TH, PH, MY, VN, GB, MX, SG, SA, BR, ES, JP, DE, IT, and FR. <br>

## Known Risks and Mitigations: <br>
Risk: API credentials and session metadata are sent to a configurable network gateway. <br>
Mitigation: Keep API keys in a controlled environment and do not set LINKFOX_TOOL_GATEWAY to untrusted hosts. <br>
Risk: Full API responses are saved locally and may contain raw product research data. <br>
Mitigation: Review where result files are written and delete saved response files when they are no longer needed. <br>
Risk: Each query consumes LinkFox/EchoTik credits, and repeated exploratory calls can add cost. <br>
Mitigation: Use the 24-hour cache for repeated parameter sets and ask before changing keywords, filters, or pagination after failed or empty results. <br>


## Reference(s): <br>
- [EchoTik-TikTok商品搜索 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-product) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell command examples, and saved JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Calls a LinkFox/EchoTik API, uses a 24-hour local cache for matching parameters, consumes 4.5 credits per query, and summarizes large responses while saving full JSON locally.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
