## Description: <br>
帮带娃家庭轻松出行，提供儿童票政策查询、亲子友好景点推荐和年龄段出行打包清单，覆盖机票火车景点三大票务场景。暑期亲子游全流程，吃住行玩一站式 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Families and travel-planning agents use this skill to check child ticket policies, find child-friendly attractions, and generate age-aware packing guidance for trips with children. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Destination names, city names, attraction keywords, and weather lookup locations are sent to external proxy services. <br>
Mitigation: Enter only the travel details needed for the query and avoid highly sensitive itinerary details. <br>
Risk: The security guidance flags the hard-coded proxy token as a publisher security issue. <br>
Mitigation: Prefer a publisher-managed environment token, rotate exposed tokens, and monitor proxy use for abuse. <br>
Risk: Ticket policies, prices, and venue requirements may differ from the skill's general guidance. <br>
Mitigation: Confirm child ticket rules and medical or safety decisions with the relevant carrier, railway operator, venue, or professional source before travel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/family-travel-assistant) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON command results that an agent can summarize as text or markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include child ticket policy guidance, attraction recommendations, packing checklist items, weather notes, and travel tips.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
