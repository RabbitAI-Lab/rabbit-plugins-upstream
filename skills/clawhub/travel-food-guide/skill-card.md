## Description: <br>
帮旅行者找景点周边餐厅、当地必吃特色、生成多日餐饮计划，旅途中不踩雷、不错过当地特色。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to find nearby restaurants, discover local specialty foods, and draft multi-day meal plans from locations, budgets, cuisines, and dietary preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel food searches and location terms are sent to the publisher proxy and the underlying map POI service. <br>
Mitigation: Install only if this data flow is acceptable, and avoid highly sensitive home, workplace, or private itinerary locations. <br>
Risk: The release includes an embedded fallback proxy token, which is a credential hygiene issue. <br>
Mitigation: The publisher should remove or rotate the fallback token and rely on a securely provided PROXY_TOKEN. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-food-guide) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Shell commands] <br>
**Output Format:** [Natural-language or Markdown response backed by JSON restaurant, specialty-food, or meal-plan results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live restaurant searches send city, location, cuisine, budget, and radius terms to the publisher proxy and map POI service; specialty-food and meal-plan responses may use bundled city food knowledge.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
