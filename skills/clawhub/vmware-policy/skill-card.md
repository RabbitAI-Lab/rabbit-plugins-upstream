## Description: <br>
Unified audit logging, policy enforcement, and input sanitization for the VMware MCP skill family. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill as shared VMware skill-family infrastructure for audit-log queries, policy-rule management, policy checks, input sanitization, and integrating the vmware_tool decorator into related VMware skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Policy enforcement can fail open or be bypassed if rules are missing, PyYAML is unavailable, or VMWARE_POLICY_DISABLED is set. <br>
Mitigation: Configure ~/.vmware/rules.yaml immediately, ensure PyYAML is installed, and restrict who can set VMWARE_POLICY_DISABLED. <br>
Risk: Audit records and exported logs may contain operational details about VMware environments. <br>
Mitigation: Protect ~/.vmware/audit.db and exported logs with least-privilege filesystem permissions and controlled sharing. <br>
Risk: Agent detection may depend on environment variables that include secret-shaped names such as OPENAI_API_KEY. <br>
Mitigation: Consider replacing API-key-based detection with an explicit non-secret marker before production use. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/zw008/VMware-Policy) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy) <br>
- [VMware Policy capabilities](references/capabilities.md) <br>
- [VMware Policy CLI reference](references/cli-reference.md) <br>
- [VMware Policy setup guide](references/setup-guide.md) <br>
- [VMware Policy agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python snippets, YAML examples, and JSON audit-export examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May refer to local audit data in ~/.vmware/audit.db, policy rules in ~/.vmware/rules.yaml, and vmware-audit CLI output.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
