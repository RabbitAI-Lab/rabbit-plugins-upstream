## Description: <br>
Use this skill whenever the user needs to manage VMware storage, including datastores, iSCSI targets, and vSAN clusters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect VMware storage, find datastore images, manage iSCSI targets, and check vSAN health or capacity through CLI and MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VMware storage operations can affect production datastores, iSCSI targets, or vSAN capacity. <br>
Mitigation: Use minimum-needed VMware RBAC, explicitly verify the target vCenter or ESXi host, and prefer dry-run before state-changing iSCSI operations. <br>
Risk: Credential material may be stored in the local vmware-storage environment file. <br>
Mitigation: Keep ~/.vmware-storage/.env locked down or use a secret manager, and avoid storing passwords in shared configuration files. <br>
Risk: Diagnostic shortcuts such as doctor --skip-auth can bypass normal connectivity and authentication checks. <br>
Mitigation: Treat skipped-auth diagnostics as last-resort troubleshooting, not as proof that a target is safe to operate on. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage) <br>
- [Project homepage](https://github.com/vmware-skills/VMware-Storage) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [VMware Storage Capabilities](references/capabilities.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown] <br>
**Output Format:** [Markdown guidance with CLI commands and MCP tool call recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference JSON-style MCP result envelopes for datastore, iSCSI, and vSAN operations.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
