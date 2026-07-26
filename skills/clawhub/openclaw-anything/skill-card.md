## Description: <br>
OpenClaw Anything helps agents install, configure, operate, and troubleshoot the OpenClaw CLI ecosystem across gateways, channels, models, agents, nodes, browser tooling, memory, security, automation, and deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doanbactam](https://clawhub.ai/user/doanbactam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to guide OpenClaw setup, gateway operation, configuration, deployment, command lookup, and maintenance workflows. It is useful when an agent needs concise OpenClaw operational guidance or shell commands while respecting the wrapper's high-risk command gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill wraps a powerful local OpenClaw management CLI that can affect gateway, channel, model, agent, service, browser, node, automation, hook, sandbox, or secret state. <br>
Mitigation: Require explicit user approval before any state-changing command and keep high-risk wrapper operations gated behind OPENCLAW_WRAPPER_ALLOW_RISKY=1. <br>
Risk: Server security review reports that the wrapper's safety gate does not cover several state-changing command families. <br>
Mitigation: Treat the wrapper as a convenience layer rather than a permission boundary and manually review commands that mutate OpenClaw state. <br>
Risk: OpenClaw workflows may involve gateway tokens, credentials, or shell environment import. <br>
Mitigation: Avoid plaintext API keys and broad shell-environment import; prefer documented secret workflows, dry runs, audits, and least-privilege gateway configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/doanbactam/skills/openclaw-anything) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai/) <br>
- [OpenClaw CLI Documentation](https://docs.openclaw.ai/cli) <br>
- [OpenClaw Gateway Security](https://docs.openclaw.ai/gateway/security) <br>
- [OpenClaw Install Documentation](https://docs.openclaw.ai/install) <br>
- [CLI Reference](references/cli-full.md) <br>
- [Security Policy](references/security-policy.md) <br>
- [Configuration Reference](references/config-schema.md) <br>
- [Deployment](references/deployment.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and reference paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands for a local OpenClaw CLI; high-risk operations require explicit user approval and OPENCLAW_WRAPPER_ALLOW_RISKY=1.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
