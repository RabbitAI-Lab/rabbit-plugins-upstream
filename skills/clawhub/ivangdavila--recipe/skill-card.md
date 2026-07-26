## Description: <br>
Build a personal recipe collection with ingredients, scaling, and meal planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to capture recipes into a local Markdown collection, search by ingredients or tags, scale servings, plan meals, and generate shopping lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update local recipe files under ~/recipes/. <br>
Mitigation: Use it for recipes you are comfortable storing locally, and ask the agent to confirm before saving or changing files. <br>
Risk: The skill may contact external recipe websites when given a URL. <br>
Mitigation: Provide only recipe URLs you are comfortable having the agent fetch, and request confirmation before network access when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/recipe) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown recipe files, meal plans, shopping lists, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update files under ~/recipes/ and may fetch recipe pages when the user provides URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
