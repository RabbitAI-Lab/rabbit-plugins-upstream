## Description: <br>
Use when the user asks an agent to send a Bark push notification, notify them from the terminal, test Bark notification delivery, or use a Bark notification skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumen01](https://clawhub.ai/user/lumen01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to send concise Bark push notifications for requested reminders, meaningful task milestones, completed long-running work, and blockers that need attention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Bark device key could be exposed through committed files, shell history, process inspection, or pasted command output. <br>
Mitigation: Keep BARK_KEY in private local config or pass it through standard input, avoid command-line keys, and use dry-run or doctor output that masks the device key. <br>
Risk: Notifications and the device key are sent through the configured Bark server. <br>
Mitigation: Use the default Bark server or set --server only when the server is trusted. <br>
Risk: An agent could send unnecessary or over-urgent notifications. <br>
Mitigation: Send notifications only for explicit requests, meaningful milestones, completion, blockers, or failures; reserve timeSensitive and critical levels for prompt action or explicit emergency use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lumen01/skills/agent-bark-notify) <br>
- [Source repository](https://github.com/Lumen01/agent-bark-notify) <br>
- [Source commit](https://github.com/Lumen01/agent-bark-notify/commit/e56a3203b4b9ac92e75e1044302ac41bf9a890ce) <br>
- [Bark project](https://github.com/Finb/Bark) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Notifications are sent through the configured Bark server; dry-run and doctor modes mask the Bark device key.] <br>

## Skill Version(s): <br>
0.1.7 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
