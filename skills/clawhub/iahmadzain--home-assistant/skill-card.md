## Description: <br>
Control Home Assistant smart home devices, run automations, and receive webhook events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iahmadzain](https://clawhub.ai/user/iahmadzain) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and smart-home users use this skill to let an agent query Home Assistant state, control entities, activate scenes, run scripts and automations, and receive automation webhook events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent control real-world Home Assistant devices and automations. <br>
Mitigation: Install only when that level of control is intended, and review proposed actions before execution. <br>
Risk: Long-lived Home Assistant tokens can expose broad account access if stored or shared insecurely. <br>
Mitigation: Use a dedicated least-privilege token where possible, store config files with owner-only permissions, and rotate tokens when access changes. <br>
Risk: The generic service caller can reach sensitive domains such as locks, alarms, covers, climate, cameras, and scripts. <br>
Mitigation: Avoid generic service calls for sensitive domains unless the action is explicit and expected. <br>


## Reference(s): <br>
- [Home Assistant Skill Page](https://clawhub.ai/iahmadzain/skills/home-assistant) <br>
- [Publisher Profile](https://clawhub.ai/user/iahmadzain) <br>
- [Home Assistant REST API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown] <br>
**Output Format:** [Markdown with inline JSON, YAML, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; uses Home Assistant URL and long-lived access token configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
