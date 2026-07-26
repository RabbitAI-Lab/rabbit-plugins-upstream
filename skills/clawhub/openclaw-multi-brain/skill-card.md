## Description: <br>
Runs secondary LLM perspectives before an OpenClaw agent responds and injects concise guidance into the agent context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannydvm](https://clawhub.ai/user/dannydvm) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to add secondary model perspectives to agent turns before the primary agent answers. It is intended for workflows where extra critique, risk checks, or alternative reasoning may improve response quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent conversations and memory or context content may be sent to configured external AI providers. <br>
Mitigation: Use local Ollama for sensitive work, enable the skill only in approved workspaces, and restrict ownerIds or session scope before deployment. <br>
Risk: The daemon can run persistently and monitor local agent session files. <br>
Mitigation: Review service installation settings, run only under a trusted user account, and stop or uninstall the daemon when the workflow no longer needs it. <br>
Risk: API keys may be stored in plaintext configuration or key files. <br>
Mitigation: Avoid production credentials until secret storage is hardened, limit key permissions where possible, and rotate keys after testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dannydvm/skills/openclaw-multi-brain) <br>
- [Publisher profile](https://clawhub.ai/user/dannydvm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown perspective text injected into agent context, with setup guidance and shell commands in documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call configured local or external LLM providers and may write latest perspective files for agent use.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact package.json and CHANGELOG report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
