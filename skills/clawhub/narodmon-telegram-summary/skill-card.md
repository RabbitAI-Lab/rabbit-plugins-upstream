## Description: <br>
Use when setting up daily sensor summary reports from narodmon.ru to Telegram, including REST API authentication, sensor history and value calls, matplotlib chart generation, Telegram Bot API photo delivery, and Hermes cron setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stshakh](https://clawhub.ai/user/stshakh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure a scheduled Narodmon sensor summary that generates a daily chart and sends it to a Telegram chat. It is intended for ongoing monitoring of Narodmon-connected temperature, pressure, humidity, or similar IoT sensors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Narodmon API traffic defaults to unencrypted HTTP while account authentication is used. <br>
Mitigation: Use HTTPS for Narodmon when it works in the deployment environment, avoid private sensors or account authentication over HTTP, and review the configuration before installing. <br>
Risk: The JSON configuration contains Narodmon credentials and Telegram delivery details. <br>
Mitigation: Restrict the config file to the owning user and verify the Telegram bot token and chat ID target only the intended destination. <br>


## Reference(s): <br>
- [Narodmon website](https://narodmon.ru) <br>
- [Narodmon API endpoint](http://api.narodmon.ru) <br>
- [ClawHub skill page](https://clawhub.ai/stshakh/skills/narodmon-telegram-summary) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, shell, and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup instructions and reusable artifact files for a scheduled Python job that writes a PNG chart path and sends the chart through Telegram.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
