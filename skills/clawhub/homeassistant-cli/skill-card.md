## Description: <br>
Advanced Home Assistant control using the official hass-cli tool, with auto-completion, event monitoring, history queries, and rich output formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joneschi](https://clawhub.ai/user/joneschi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to operate and explore Home Assistant smart-home entities through hass-cli, including device control, event monitoring, service discovery, and state history queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Home Assistant token that can authorize broad smart-home actions. <br>
Mitigation: Use a dedicated or least-privileged Home Assistant account where possible and keep HASS_TOKEN out of logs, screenshots, shell history, and synced dotfiles. <br>
Risk: Generated hass-cli commands can affect alarms, locks, covers, climate systems, appliances, or automations. <br>
Mitigation: Review commands before execution, especially commands that change security, access, climate, appliance, or automation state. <br>


## Reference(s): <br>
- [Home Assistant CLI skill page](https://clawhub.ai/joneschi/skills/homeassistant-cli) <br>
- [Home Assistant CLI project](https://github.com/home-assistant-ecosystem/home-assistant-cli) <br>
- [Auto-completion Setup](references/autocomplete.md) <br>
- [Home Assistant CLI Examples](references/examples.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that read or change Home Assistant entity state through hass-cli.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
