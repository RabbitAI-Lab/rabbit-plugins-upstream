## Description: <br>
Daily weather briefing for any city: morning conditions, clothing and umbrella guidance, evening previews, weekly forecasts, and extreme weather alerts without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Weather Daily to generate city-specific weather briefings, push schedules, and forecast prompts for morning, evening, weekly, and monthly weather updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad weather trigger phrases may activate the skill for general weather requests. <br>
Mitigation: Review activation behavior during installation and adjust usage if it responds outside the intended weather workflow. <br>
Risk: Weather output depends on live web search results and may not match official alert status. <br>
Mitigation: Check official meteorological sources before relying on extreme weather warnings or travel guidance. <br>
Risk: Chinese and English output may not match the user's expected language if automatic language selection is wrong. <br>
Mitigation: Confirm the configured language and pass an explicit language option when running scripts or enabling pushes. <br>


## Reference(s): <br>
- [Weather Daily on ClawHub](https://clawhub.ai/jiajiaoy/skills/weather-daily) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates bilingual weather-search prompts and push configuration messages; it does not fetch weather data directly.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release, package.json, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
