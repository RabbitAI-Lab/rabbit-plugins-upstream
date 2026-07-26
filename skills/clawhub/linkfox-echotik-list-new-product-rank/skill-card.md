## Description: <br>
Queries EchoTik data so agents can retrieve and present daily TikTok Shop new-product rankings across 16 regional markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, analysts, and developers use this skill to look up TikTok Shop new-product ranking data for product scouting, trend analysis, and competitive intelligence. The skill is scoped to daily EchoTik ranking snapshots and presents product metrics such as sales, revenue, price, creator coverage, live activity, ratings, and image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a LinkFox API key, makes paid external API calls, and may share query parameters and session metadata with the configured LinkFox tool gateway. <br>
Mitigation: Install only when this access is acceptable, confirm cost before repeated calls, and review or constrain LINKFOX_TOOL_GATEWAY. <br>
Risk: Full product-ranking responses are retained on disk in local linkfox cache and output folders. <br>
Mitigation: Clear the linkfox cache and output folders when the ranking data should not persist. <br>
Risk: Feedback reporting can send user-provided feedback content to the LinkFox feedback API. <br>
Mitigation: Avoid including secrets, private business data, or unnecessary sensitive details in feedback. <br>


## Reference(s): <br>
- [EchoTik-TikTok新品榜 API Reference](references/api.md) <br>
- [ClawHub skill release page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-new-product-rank) <br>
- [LinkFox EchoTik API endpoint](https://tool-gateway.linkfox.com/echotik/listNewProductRank) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, tabular result summaries, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, consumes 4.5 credits per lookup, caches identical parameter calls for 24 hours, and writes full API responses to local linkfox data folders.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
