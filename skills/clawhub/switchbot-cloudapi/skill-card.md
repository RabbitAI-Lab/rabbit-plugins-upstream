## Description: <br>
Controls and queries SwitchBot devices through OpenAPI v1.1, including device status, commands, scenes, family and room views, and AI MindClip recordings, summaries, and todos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[switchbot-dev](https://clawhub.ai/user/switchbot-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and smart-home users use this skill to let an agent inspect and control authorized SwitchBot devices and retrieve AI MindClip data through authenticated API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control locks, garage doors, keypad passcodes, scenes, and automations through the user's SwitchBot account. <br>
Mitigation: Require explicit user confirmation before unlock, garage, keypad, scene, or automation actions, and use the skill only for devices the user owns or is authorized to control. <br>
Risk: AI MindClip commands can expose transcripts, summaries, todos, daily memories, weekly summaries, and location-related private data. <br>
Mitigation: Access only authorized MindClip data, avoid unnecessary display of sensitive content, and do not log transcripts, locations, or summaries. <br>
Risk: SwitchBot API credentials grant account authority if exposed. <br>
Mitigation: Provide SWITCHBOT_TOKEN and SWITCHBOT_SECRET through secure environment variables and avoid printing, storing, or hardcoding them. <br>


## Reference(s): <br>
- [SwitchBot Commands Reference](references/commands.md) <br>
- [SwitchBot API Examples](references/examples.md) <br>
- [SwitchBot OpenAPI Base Endpoint](https://api.switch-bot.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/switchbot-dev/skills/switchbot-cloudapi) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SWITCHBOT_TOKEN and SWITCHBOT_SECRET; some commands can change physical smart-home device state.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
