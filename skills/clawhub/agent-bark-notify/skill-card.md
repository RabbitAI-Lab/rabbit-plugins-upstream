## Description: <br>
Sends Bark push notifications from agents, including terminal notifications, delivery checks, and configurable notification metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumen01](https://clawhub.ai/user/lumen01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to send Bark notifications for explicit requests, meaningful task milestones, completion events, and blockers while keeping Bark credentials in local private configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification titles and bodies are sent to the configured Bark server. <br>
Mitigation: Use the skill only for content appropriate to send through Bark, and avoid putting sensitive information in notification text. <br>
Risk: A Bark device key can be exposed if supplied on the command line or committed in repository files. <br>
Mitigation: Keep the key in the private local config file or provide it through stdin setup, and avoid command-line key arguments. <br>
Risk: A global agent instruction can cause multiple agents to send notifications proactively. <br>
Mitigation: Enable proactive notification instructions only where wanted, and limit pushes to explicit requests, meaningful milestones, completion events, and blockers. <br>


## Reference(s): <br>
- [Agent Bark Notify on ClawHub](https://clawhub.ai/lumen01/skills/agent-bark-notify) <br>
- [Bark project](https://github.com/Finb/Bark) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; CLI checks may print JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled CLI can send notifications, perform ping and doctor checks, and print masked dry-run payloads.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
