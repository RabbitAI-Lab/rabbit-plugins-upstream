## Description: <br>
Helps agents manage VMware NSX distributed firewall policies and rules, security groups, VM tags, Traceflow diagnostics, and IDS/IPS status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Infrastructure, network security, and platform engineers use this skill to administer NSX security controls, validate microsegmentation behavior, inspect firewall policy state, and run controlled diagnostics from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent use can administer sensitive NSX firewall and security objects. <br>
Mitigation: Install only for intended NSX security administration, use a dedicated least-privilege NSX account, and require explicit approval for write operations. <br>
Risk: NSX target credentials and local configuration may expose privileged access if handled loosely. <br>
Mitigation: Prefer environment injection or a secret manager over a plaintext .env file for production, and keep config and .env files owner-only. <br>
Risk: Firewall rule, security group, tag, or diagnostic write actions can change network enforcement or inject trace packets. <br>
Mitigation: Use dry-run and review flows where available, rely on audit logging for state changes, and validate proposed changes before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-nsx-security) <br>
- [Publisher Profile](https://clawhub.ai/user/zw008) <br>
- [Project Homepage](https://github.com/zw008/VMware-NSX-Security) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute NSX security administration actions through CLI or MCP tools when configured; write actions require appropriate user approval and environment credentials.] <br>

## Skill Version(s): <br>
1.8.8 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
