## Description: <br>
Queries daily horoscope details for the twelve zodiac signs, including overall, love, work, finance, health, lucky color, lucky number, and a daily summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to fetch and summarize TianAPI daily horoscope results for a requested zodiac sign and optional date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends horoscope query parameters and the user's TianAPI API key to TianAPI. <br>
Mitigation: Use the skill only when sharing those parameters with TianAPI is acceptable, and keep the API key in an environment variable or secret manager. <br>
Risk: Passing the API key on the command line or storing it in scripts/.env can expose credentials through shell history, process listings, or source control. <br>
Mitigation: Prefer TIANAPI_STAR_KEY or a secret manager, avoid command-line key arguments, and do not commit scripts/.env. <br>


## Reference(s): <br>
- [TianAPI Star Horoscope API](https://www.tianapi.com/apiview/78) <br>
- [TianAPI Star API endpoint](https://apis.tianapi.com/star/index) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-star) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI API key supplied through TIANAPI_STAR_KEY, a local scripts/.env file, or a command-line option.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
