## Description: <br>
Load and analyze Strava activities, stats, and workouts using the Strava API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bohdanpodvirnyi](https://clawhub.ai/user/bohdanpodvirnyi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to help an agent retrieve Strava activities, athlete profile data, workout details, and training statistics through authenticated Strava API requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Strava OAuth tokens and client secrets that can expose private activity and account data if printed, logged, shared, or committed. <br>
Mitigation: Treat Strava credentials as passwords, keep them out of shared terminals and version control, restrict local file access, and revoke or rotate credentials if token output is exposed. <br>
Risk: The token refresh script can display newly issued access and refresh tokens in terminal output. <br>
Mitigation: Run token refresh only in trusted local sessions and avoid retaining logs that contain token values. <br>


## Reference(s): <br>
- [Strava Skill on ClawHub](https://clawhub.ai/bohdanpodvirnyi/skills/strava) <br>
- [Strava Developers](https://developers.strava.com/) <br>
- [Strava API Reference](https://developers.strava.com/docs/reference/) <br>
- [Create a Strava API Application](https://www.strava.com/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Strava API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Strava API response data when commands are executed with user-provided credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
