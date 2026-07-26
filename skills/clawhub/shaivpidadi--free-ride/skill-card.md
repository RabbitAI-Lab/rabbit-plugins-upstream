## Description: <br>
Manages free AI models from OpenRouter for OpenClaw by ranking available free models, configuring fallback routing for rate-limit handling, and updating OpenClaw model settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaivpidadi](https://clawhub.ai/user/shaivpidadi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure OpenRouter free models, choose a primary model, and maintain fallback model routing when rate limits or unavailable models interrupt agent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change OpenClaw default and fallback model routing. <br>
Mitigation: Back up ~/.openclaw/openclaw.json before use and review the model settings after running FreeRide commands. <br>
Risk: The optional watcher may continue making OpenRouter requests and rewriting model settings until it is stopped. <br>
Mitigation: Run freeride-watcher only when continuous background recovery is intended, monitor its state or logs, and stop the process when unattended routing changes are no longer needed. <br>
Risk: The skill requires an OpenRouter API key. <br>
Mitigation: Keep OPENROUTER_API_KEY private and configure it only in trusted shell or OpenClaw environments. <br>


## Reference(s): <br>
- [ClawHub Free Ride release](https://clawhub.ai/shaivpidadi/skills/free-ride) <br>
- [Publisher profile](https://clawhub.ai/user/shaivpidadi) <br>
- [OpenRouter API keys](https://openrouter.ai/keys) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct the agent to run FreeRide CLI commands that update OpenClaw model configuration and cache model data.] <br>

## Skill Version(s): <br>
1.0.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
