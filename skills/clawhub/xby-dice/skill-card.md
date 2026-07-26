## Description: <br>
An MCP skill that lets an agent roll dice using standard notation such as 1d20 and return the roll result and total. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users can ask an agent to resolve tabletop or game dice notation through the XiaoBenYang service when a configured XBY API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores an XBY API key in a local .env file. <br>
Mitigation: Use a scoped API key where possible, avoid sharing the workspace, and remove the .env entry when the skill is no longer needed. <br>
Risk: Dice requests and the configured API key are sent to a remote XiaoBenYang service. <br>
Mitigation: Install only when the publisher and service are trusted for the intended use, and avoid sending sensitive prompts or data through dice notation requests. <br>
Risk: The artifact contains leftover exam-service naming and code paths unrelated to a dice roller. <br>
Mitigation: Review the artifact before installation and prefer a release that removes unrelated exam-service leftovers and limits behavior to the dice function. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-dice) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration] <br>
**Output Format:** [Markdown text summarizing JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and sends dice requests to a remote XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
