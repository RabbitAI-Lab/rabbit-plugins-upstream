## Description: <br>
Runtime safety guard for OpenClaw multi-agent workflows that blocks selected destructive tools for controlled agents and redirects work to sub-agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ifeel-is-a-mouse](https://clawhub.ai/user/ifeel-is-a-mouse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators of OpenClaw multi-agent workflows use Mainctrl to keep orchestration agents from making direct destructive changes while still allowing delegated implementation work through sub-agents. It is useful when runtime tool-access controls need to be toggled or configured without changing agent behavior globally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat Mainctrl as a security boundary even though the security evidence describes it as a delegation aid. <br>
Mitigation: Use it as an administrative guardrail, not as a sandbox; review OpenClaw permissions and plugin behavior before relying on it in sensitive workflows. <br>
Risk: The guard can be turned off, and missing or corrupt state falls back to permissive behavior. <br>
Mitigation: Check Mainctrl status after installation, restart, and configuration changes; verify blocking is on before starting workflows that depend on it. <br>
Risk: Sub-agents remain able to write and execute, so delegated work can still make destructive changes. <br>
Mitigation: Configure controlled agents and blocked tools deliberately, and review sub-agent permissions for the intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ifeel-is-a-mouse/skills/mainctrl) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact plugin manifest](artifact/plugin/openclaw.plugin.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-invoked administrative guidance and command/configuration updates for OpenClaw tool-routing controls.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
