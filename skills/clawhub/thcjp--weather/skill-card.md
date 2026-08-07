## Description: <br>
The Weather skill helps agents answer current weather and forecast requests for a user-specified city or region. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request weather status or forecasts through an agent and review the returned conditions before acting on them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact requests broad read, write, and command execution permissions for a weather lookup skill. <br>
Mitigation: Review the skill carefully before installation and prefer a version limited to weather queries without exec or write access. <br>
Risk: The artifact gives inconsistent API-key requirements, including both no-key claims and API_KEY setup guidance. <br>
Mitigation: Confirm the required setup path before deployment and publish consistent credential instructions. <br>


## Reference(s): <br>
- [ClawHub weather skill page](https://clawhub.ai/thcjp/skills/weather) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact describes weather query inputs and may include configuration guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
