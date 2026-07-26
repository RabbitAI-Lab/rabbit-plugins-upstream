## Description: <br>
Control Roku devices via CLI with discovery, remote control, app launching, search, and HTTP bridge mode for real-time control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and home automation users can use this skill to discover Roku devices, send remote-control actions, launch apps, type text, and configure local bridge control for a Roku on the same network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real Roku devices and may affect playback, app state, text entry, or power-related controls. <br>
Mitigation: Install only when the machine is intended to control the Roku, and restrict use to trusted local users. <br>
Risk: Bridge or service setup can create a persistent control path. <br>
Mitigation: Review service setup before enabling it, keep the bridge bound to localhost unless intentional exposure is required, and use authentication tokens for bridge mode. <br>
Risk: Telegram integration can route remote button presses through a bot token. <br>
Mitigation: Protect Telegram bot tokens and restrict commands and IPC permissions to the intended local user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/roku) <br>
- [npm package @gumadeiras/roku](https://www.npmjs.com/package/@gumadeiras/roku) <br>
- [Roku CLI repository](https://github.com/gumadeiras/roku-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local device-control commands, service setup steps, and authenticated localhost bridge examples.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
