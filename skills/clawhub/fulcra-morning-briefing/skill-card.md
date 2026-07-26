## Description: <br>
Fulcra Morning Briefing helps agents compose personalized morning briefings from Fulcra sleep, biometric, calendar, activity, and weather context, with tone and detail calibrated to recent sleep quality. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect Fulcra sleep, biometric, calendar, activity, and weather context and compose a private morning briefing calibrated to recent sleep quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive sleep, health, calendar, wearable, and location context. <br>
Mitigation: Install only when that data use is acceptable, keep briefings private by default, and review generated summaries before sharing. <br>
Risk: Weather lookup may send the configured location to a third-party weather service. <br>
Mitigation: Use weather only with user consent, prefer an explicit coarse location, or disable the weather portion when location sharing is not acceptable. <br>
Risk: The workflow depends on shell and network access to collect context. <br>
Mitigation: Run it in a trusted environment, review the Fulcra CLI and weather commands before deployment, and constrain command paths where possible. <br>


## Reference(s): <br>
- [Fulcra Platform](https://fulcradynamics.com) <br>
- [Fulcra Developer Docs](https://docs.fulcradynamics.com) <br>
- [Fulcra Python Client](https://github.com/fulcradynamics/fulcra-api-python) <br>
- [Context iOS App](https://apps.apple.com/app/id1633037434) <br>
- [Fulcra Morning Briefing on ClawHub](https://clawhub.ai/arc-claw-bot/skills/fulcra-morning-briefing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown briefing guidance with shell command examples and JSON collector output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Collector output may include private Fulcra context and should be reviewed before sharing.] <br>

## Skill Version(s): <br>
1.1.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
