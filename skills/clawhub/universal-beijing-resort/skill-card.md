## Description: <br>
北京环球影城一站式游园助手，提供实时排队查询、下一步推荐、路线规划、演出时间、营业时间、餐厅推荐和门票价格查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to plan visits to Universal Beijing Resort, including checking public wait-time and schedule data, choosing attractions, planning one-day routes, estimating ticket options, and finding dining suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live wait-time and operating-hours answers depend on themeparks.wiki public API availability and freshness. <br>
Mitigation: Treat live schedule and wait-time responses as planning guidance and confirm time-sensitive details with Universal Beijing Resort's official channels before acting. <br>
Risk: Route, dining, show, and ticket recommendations are partly based on local preset data and may not reflect current prices, closures, or event changes. <br>
Mitigation: Use the skill for itinerary planning, then verify purchases, reservations, prices, and same-day park rules through official Universal Beijing Resort sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/universal-beijing-resort) <br>
- [ThemeParks.wiki public API](https://api.themeparks.wiki/) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, API calls] <br>
**Output Format:** [Plain text or Markdown-style Chinese guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool outputs may combine public themeparks.wiki live data with local preset estimates for routes, dining, shows, and ticket guidance.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
