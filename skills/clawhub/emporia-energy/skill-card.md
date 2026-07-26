## Description: <br>
Direct Emporia Vue energy queries via Emporia cloud (PyEmVue) or local ESPHome API, including guidance on choosing/configuring cloud vs local modes and running list/summary/circuit commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[urosorozel](https://clawhub.ai/user/urosorozel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and home-energy users use this skill to configure cloud or local access to Emporia Vue data and ask an agent to list channels, summarize usage, or query specific circuits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Emporia account credentials or ESPHome API secrets for cloud or local energy queries. <br>
Mitigation: Keep credentials in environment variables or local configuration and avoid sharing them in chat, logs, or public outputs. <br>
Risk: Device names, circuit names, and energy readings may reveal household usage details. <br>
Mitigation: Review JSON output before sharing and redact device, circuit, or usage details when they could expose private activity patterns. <br>
Risk: The ESPHome dependency is specified as a version range rather than an exact pinned release. <br>
Mitigation: Pin aioesphomeapi to an exact reviewed version in deployments that require stricter repeatability. <br>
Risk: Energy readings can support monitoring decisions but do not validate electrical safety or wiring. <br>
Mitigation: Limit the skill to data querying and configuration guidance, and defer panel or wiring recommendations to qualified professionals. <br>


## Reference(s): <br>
- [Emporia Energy ClawHub Release](https://clawhub.ai/urosorozel/skills/emporia-energy) <br>
- [urosorozel ClawHub Profile](https://clawhub.ai/user/urosorozel) <br>
- [Emporia Energy Skill References](references/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts emit JSON including timestamp, unit, total usage, top circuits, and channels used.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
