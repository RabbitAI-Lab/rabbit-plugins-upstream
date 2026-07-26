## Description: <br>
Predict satellite passes for NOAA APT, METEOR LRPT, and ISS over a configured location, then send WhatsApp alerts with manual dish alignment details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davestarling](https://clawhub.ai/user/davestarling) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, radio hobbyists, and SDR operators use this skill to configure a local satellite-pass scheduler, receive pass timing and antenna-pointing alerts, and prepare optional SDR capture and decode automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A scheduled local notifier can send alerts to the wrong recipient or for the wrong observation location if configuration is copied without review. <br>
Mitigation: Verify the WhatsApp target, observer latitude and longitude, and cron schedule before enabling recurring runs. <br>
Risk: Optional capture and decode hooks can execute configured commands with the local user's privileges and inherited environment. <br>
Mitigation: Keep capture and decode hooks disabled until each command is fully trusted, scoped, and tested with appropriate timeouts. <br>


## Reference(s): <br>
- [Satellite Copilot on ClawHub](https://clawhub.ai/davestarling/skills/moltbot-satellite-copilot) <br>
- [TLE data API used by the predictor](https://tle.ivanstanojevic.me/api/tle/${norad}) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, text, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration; runtime scripts emit WhatsApp text alerts and JSONL pass data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local configuration for observer location, satellites, notification target, and optional capture/decode hooks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
