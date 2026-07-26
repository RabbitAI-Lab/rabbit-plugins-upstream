## Description: <br>
Control Amazon Alexa devices and smart home via the `alexacli` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buddyh](https://clawhub.ai/user/buddyh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent list Alexa devices, speak or announce through Echo devices, send smart-home voice commands, query Alexa responses, play audio, and inspect Alexa history or conversation data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad smart-home and Alexa account access. <br>
Mitigation: Require explicit user confirmation before commands involving locks, thermostats, alarms, purchases, or whole-home announcements. <br>
Risk: Alexa calendar, history, and conversation outputs may contain private information. <br>
Mitigation: Treat returned account data as private and avoid exposing it outside the active user request. <br>
Risk: The alexacli configuration stores credentials locally in ~/.alexa-cli/config.json. <br>
Mitigation: Protect the configuration file and remove it with `alexacli auth logout` or by deleting it when access is no longer needed. <br>
Risk: The skill depends on the third-party alexacli upstream project and an unofficial Alexa API. <br>
Mitigation: Install only when the upstream project is trusted and re-check behavior after upstream or Alexa service changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/buddyh/skills/alexa-cli) <br>
- [Publisher Profile](https://clawhub.ai/user/buddyh) <br>
- [Alexa CLI Homepage](https://github.com/buddyh/alexa-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include commands that control Alexa devices, smart-home equipment, account data, and local alexacli configuration.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
