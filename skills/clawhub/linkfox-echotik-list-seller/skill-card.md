## Description: <br>
Searches and analyzes TikTok Shop sellers across 16 marketplaces with filters for region, category, GMV, sales trend, listing date, and store type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and e-commerce analysts use this skill to discover and benchmark TikTok Shop stores by marketplace, category, revenue, sales trend, listing date, and local or cross-border status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires LinkFox/EchoTik API access for TikTok Shop seller lookups. <br>
Mitigation: Install and run it only when the user is comfortable providing LinkFox API credentials for this purpose. <br>
Risk: Full API results and query history may be written under local linkfox directories. <br>
Mitigation: Treat saved response files as potentially sensitive workspace data and remove or restrict them according to local retention expectations. <br>
Risk: The LINKFOX_TOOL_GATEWAY environment variable can redirect requests to a different endpoint. <br>
Mitigation: Keep LINKFOX_TOOL_GATEWAY unset unless the endpoint is intentionally configured and trusted. <br>
Risk: Vague store-search requests can spend credits or send feedback externally. <br>
Mitigation: Confirm ambiguous searches before running additional API calls or reporting feedback. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-seller) <br>
- [EchoTik-TikTok店铺列表 API 参考](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown summaries with saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under linkfox session data paths; large responses print summaries unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
