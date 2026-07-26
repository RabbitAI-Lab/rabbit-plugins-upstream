## Description: <br>
Provides player props, fixtures, and live scores from propzapi.com in normalized JSON across sportsbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paperandbeyond23-gif](https://clawhub.ai/user/paperandbeyond23-gif) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when they need sourced sports player props, fixtures, schedules, or live scores through Propzapi, without betting advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Propzapi API calls require a PROPZAPI_KEY and may consume paid Propzapi credits. <br>
Mitigation: Set the key only in the intended runtime and monitor Propzapi credit usage before high-volume calls. <br>
Risk: Sports props and odds are informational and may be delayed. <br>
Mitigation: Use returned numbers as sourced data only, and avoid presenting them as betting advice. <br>


## Reference(s): <br>
- [Propzapi homepage](https://propzapi.com) <br>
- [ClawHub skill page](https://clawhub.ai/paperandbeyond23-gif/skills/propzapi-props) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON objects or error dictionaries returned from Propzapi API calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROPZAPI_KEY; Propzapi calls may consume credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
