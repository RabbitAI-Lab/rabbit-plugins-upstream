## Description: <br>
Manages free AI models from OpenRouter for OpenClaw by ranking free models, configuring rate-limit fallbacks, and updating OpenClaw model settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to route OpenClaw through OpenRouter free models, keep a ranked fallback chain, and recover when selected models are rate-limited. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change OpenClaw's active model and fallback chain. <br>
Mitigation: Back up ~/.openclaw/openclaw.json before running FreeRide and review the model settings after commands that change configuration. <br>
Risk: The skill uses an OpenRouter API key and makes live OpenRouter requests. <br>
Mitigation: Store the API key carefully, confirm OpenRouter network access is expected, and avoid exposing the key in logs or shared shell history. <br>
Risk: The watcher can run unattended while probing and rotating models. <br>
Mitigation: Run freeride-watcher only when unattended recovery is desired, supervise the process explicitly, and stop it when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xiiang0529/skills/free-ride) <br>
- [OpenRouter API Key Setup](https://openrouter.ai/keys) <br>
- [OpenRouter Models API](https://openrouter.ai/api/v1/models) <br>
- [OpenClaw Project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENROUTER_API_KEY; may update ~/.openclaw/openclaw.json, ~/.openclaw/.freeride-cache.json, and ~/.openclaw/.freeride-watcher-state.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
