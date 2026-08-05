## Description: <br>
Unified audit logging, policy enforcement, and input sanitization for the VMware MCP skill family. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to query VMware skill audit trails, configure policy rules, export audit records, sanitize untrusted VMware API text, and integrate the shared policy decorator into related VMware skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Policy enforcement can be bypassed with VMWARE_POLICY_DISABLED, so it should not be treated as a strong enforcement boundary by itself. <br>
Mitigation: Restrict who can set the environment variable, monitor ok_bypassed audit status, and use independent approval or control paths for high-impact VMware changes. <br>
Risk: Audit logs and exported records may contain sensitive operational metadata. <br>
Mitigation: Protect ~/.vmware/audit.db and exported audit files with least-privilege filesystem permissions and appropriate retention handling. <br>
Risk: Policy rules are optional, and missing policy dependencies can allow operations while audit logging continues. <br>
Mitigation: Verify ~/.vmware/rules.yaml is present, valid YAML, hot-reloaded, and enforced in the target environment before relying on policy checks. <br>


## Reference(s): <br>
- [VMware Policy Setup Guide](references/setup-guide.md) <br>
- [VMware Policy CLI Reference](references/cli-reference.md) <br>
- [VMware Policy Capabilities](references/capabilities.md) <br>
- [VMware Policy Agent Guardrails](references/agent-guardrails.md) <br>
- [Project homepage](https://github.com/vmware-skills/VMware-Policy) <br>
- [ClawHub listing](https://clawhub.ai/zw008/skills/vmware-policy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell, Python, YAML, and JSON examples; CLI workflows can emit text tables or JSON audit exports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill does not expose MCP tools directly; it provides a Python library and vmware-audit CLI used by the VMware skill family.] <br>

## Skill Version(s): <br>
1.8.9 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
