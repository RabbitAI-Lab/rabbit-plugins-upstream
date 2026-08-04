## Description: <br>
OpenClaw Switch helps users manage multi-provider model switching and fallback chains in OpenClaw by setting up automatic model failover, switching primary models, viewing fallback chains, and configuring heartbeat or subagent routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to inspect configured models, switch a primary model, and understand fallback routing across providers. It is useful for local model failover, cost optimization, and routing visibility in OpenClaw configurations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted OpenClaw configuration values could trigger code injection in the local switching script. <br>
Mitigation: Review the script before installing, back up ~/.openclaw/openclaw.json, use only trusted config files and model IDs, and prefer a patched implementation that passes paths and model IDs to Python through argv or environment variables. <br>


## Reference(s): <br>
- [OpenClaw project](https://github.com/anthropics/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and terminal text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Updates the local OpenClaw JSON configuration when the switch command is run.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
