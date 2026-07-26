## Description: <br>
Guides developers in creating Claude Code and Claude Agent SDK hooks with security-first validation, enforcement, observability, and performance practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to author, validate, test, and harden hooks for Claude Code and Claude Agent SDK workflows. It supports hook selection, configuration, security controls, logging, context injection, performance tuning, and testing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copied hook examples may log raw prompts, tool inputs, or secrets. <br>
Mitigation: Redact sensitive values and avoid raw prompt or tool-input logging before deploying examples. <br>
Risk: HTTP hooks can send hook payloads to untrusted or insecure endpoints. <br>
Mitigation: Use HTTPS and trusted endpoints, and review what data is sent before enabling HTTP hooks. <br>
Risk: Context injection or auto-approval hooks can expose project files or permit sensitive actions too broadly. <br>
Mitigation: Require user consent for project-file injection and use narrow allowlists plus review for any auto-approval behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-hook-authoring) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Claude Code hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) <br>
- [Claude Agent SDK documentation](https://docs.anthropic.com/en/docs/claude-agent-sdk) <br>
- [Claude Code settings documentation](https://docs.anthropic.com/en/docs/claude-code/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON, Python, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Markdown-only guide; examples should be reviewed and hardened before active hook use.] <br>

## Skill Version(s): <br>
1.9.16 (source: evidence release.version; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
