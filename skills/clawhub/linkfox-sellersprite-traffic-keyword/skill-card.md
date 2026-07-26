## Description: <br>
查询 Amazon ASIN 的 SellerSprite 流量关键词、流量来源占比、自然和广告排名、转化类型以及历史月份指标。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect how an Amazon ASIN receives keyword traffic through SellerSprite data, including organic and ad positions, traffic share, conversion type, and optional historical month filters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASIN queries and session metadata are sent to LinkFox/SellerSprite services. <br>
Mitigation: Install only if this external sharing is acceptable, use a trusted LINKFOX_TOOL_GATEWAY value, and avoid placing sensitive notes in feedback. <br>
Risk: Calls can consume SellerSprite or LinkFox credits. <br>
Mitigation: Confirm expected cost before repeated pagination or uncached calls, and use the skill's cache where appropriate. <br>
Risk: Full responses and cache files are saved locally and may retain query history. <br>
Mitigation: Periodically delete the linkfox output and cache directories when local retention is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-traffic-keyword) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [SellerSprite traffic keyword API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved locally; large responses print summaries unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
