## Description: <br>
Controls SwitchBot smart home devices such as curtains, plugs, lights, locks, and sensors through the SwitchBot Cloud API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to set up credentials, discover SwitchBot devices, and ask an agent to control or check supported smart home devices through the SwitchBot Cloud API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control physical SwitchBot devices, including locks and powered appliances. <br>
Mitigation: Require explicit user confirmation before lock, unlock, plug, appliance, or other safety-sensitive actions. <br>
Risk: Persistent SwitchBot API credentials enable ongoing device control from the local machine. <br>
Mitigation: Prefer a managed secret store over a plaintext credentials file and keep any local credentials file restricted to the owning user. <br>
Risk: The generic raw command mode can send broad commands to supported devices. <br>
Mitigation: Restrict or avoid raw command mode unless the command and target device have been reviewed. <br>


## Reference(s): <br>
- [Switchbot ClawHub skill page](https://clawhub.ai/daaab/skills/switchbot) <br>
- [SwitchBot Cloud API endpoint](https://api.switch-bot.com/v1.1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of a local credentials file and execute SwitchBot Cloud API requests when credentials and device IDs are available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
