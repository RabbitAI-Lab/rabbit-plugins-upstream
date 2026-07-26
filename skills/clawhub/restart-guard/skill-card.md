## Description: <br>
Deterministic OpenClaw gateway restart with down/up state-machine verification, origin-session proactive ACK, and backward-compatible config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zjianru](https://clawhub.ai/user/zjianru) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators who run OpenClaw gateways use Restart Guard to perform controlled restarts, preserve restart context, verify down/up health transitions, and report the result back to the originating session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically restart an OpenClaw gateway. <br>
Mitigation: Review the configuration first and require an explicit operational confirmation process before production restarts. <br>
Risk: Status or diagnostics may be sent to external notification channels. <br>
Mitigation: Keep notification channels disabled unless needed and use only trusted webhook or channel destinations. <br>
Risk: Gateway credentials and notification secrets may be present in the OpenClaw environment. <br>
Mitigation: Protect ~/.openclaw/.env and restrict access to GATEWAY_AUTH_TOKEN and channel credentials. <br>


## Reference(s): <br>
- [Restart Guard on ClawHub](https://clawhub.ai/zjianru/skills/restart-guard) <br>
- [README](README.md) <br>
- [Enhanced Restart Implementation Spec](ENHANCED_RESTART_IMPLEMENTATION_SPEC.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus generated JSON and Markdown restart context or diagnostic files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, curl, GATEWAY_AUTH_TOKEN, and configured notification credentials only for enabled external channels.] <br>

## Skill Version(s): <br>
2.2.0 (source: SKILL.md frontmatter, CHANGELOG.md, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
