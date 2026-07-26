## Description: <br>
Comprehensive diagnostic, error-fixing, and skill recommendation tool for OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phenixstar](https://clawhub.ai/user/phenixstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to diagnose OpenClaw errors, run health checks, apply guided or automated fixes, set up OpenClaw, and find relevant ClawHub skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repair and setup flows can make broad local or network-facing changes. <br>
Mitigation: Start with dry-run or check-only modes, review each proposed action, and keep backups of relevant OpenClaw configuration before applying fixes. <br>
Risk: Auto-fix actions may change configuration, restart services, terminate port owners, or install supporting tools. <br>
Mitigation: Run auto-fix only in an environment where those changes are acceptable, and require operator review for any action beyond read-only diagnostics. <br>
Risk: Generated or modified gateway configuration may be unsafe to use as-is on a networked machine. <br>
Mitigation: Review bind addresses, ports, credentials, and channel settings before exposing the gateway beyond a local or controlled environment. <br>
Risk: Diagnostic outputs can contain API keys, tokens, or other credentials. <br>
Mitigation: Redact secrets before sharing reports, logs, terminal output, or generated recommendations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/phenixstar/skills/openclaw-doctor-pro) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/phenixstar) <br>
- [Error Catalog](references/error-catalog.md) <br>
- [Auto-Fix Capabilities](references/auto-fix-capabilities.md) <br>
- [Diagnostic Commands](references/diagnostic-commands.md) <br>
- [Troubleshooting Workflow](references/troubleshooting-workflow.md) <br>
- [ClawHub Integration](references/clawhub-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce diagnostic reports, skill recommendations, and proposed or executed repair actions.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
