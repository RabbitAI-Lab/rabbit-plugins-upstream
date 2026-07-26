## Description: <br>
Helps agents inspect and manage VMware AVI/NSX Advanced Load Balancer and AKO Kubernetes operations, including virtual services, pool members, SSL expiry, analytics, service engines, ingress diagnostics, sync checks, and guarded state changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to troubleshoot and administer AVI Controller load balancing and AKO Kubernetes ingress workflows from an agent, including read-only diagnostics and confirmation-gated writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect and change AVI or AKO state in infrastructure environments. <br>
Mitigation: Install only where the agent is authorized for AVI and AKO administration, use read-only service accounts when possible, and require explicit confirmation for write operations. <br>
Risk: Controller credentials and audit data may be sensitive if stored in local configuration files. <br>
Mitigation: Keep ~/.vmware-avi/.env and ~/.vmware/audit.db owner-only, prefer a secret manager for passwords, and never commit environment files. <br>
Risk: Disabling TLS verification can hide connection interception or controller identity problems. <br>
Mitigation: Keep TLS verification enabled for production and disable it only for lab or self-signed test environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-avi) <br>
- [Project homepage](https://github.com/zw008/VMware-AVI) <br>
- [VMware AVI setup guide](references/setup-guide.md) <br>
- [VMware AVI capabilities](references/capabilities.md) <br>
- [VMware AVI CLI reference](references/cli-reference.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured CLI or MCP results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include environment-specific AVI, AKO, Kubernetes, and audit details returned by tools; write operations are confirmation-gated and audited.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
