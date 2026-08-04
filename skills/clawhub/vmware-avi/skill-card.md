## Description: <br>
VMware AVI helps agents administer AVI/NSX Advanced Load Balancer and AKO Kubernetes environments, including virtual services, pool members, SSL expiry, analytics, service engine health, ingress diagnostics, sync checks, and controlled write operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to inspect and operate VMware AVI/NSX ALB and AKO-backed Kubernetes ingress environments, including routine health checks, troubleshooting, maintenance-window actions, and configuration reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform live AVI and AKO write actions that may affect load balancing, ingress behavior, or Kubernetes-to-controller synchronization. <br>
Mitigation: Use least-privilege controller and Kubernetes accounts, keep production deny rules in vmware-policy, and require review before confirmed actions or non-dry-run upgrades. <br>
Risk: Credential or kubeconfig scope that is broader than the operator needs can expand the impact of mistakes or misuse. <br>
Mitigation: Use scoped service accounts, protect the .env file, prefer secret-manager injection for passwords, and install the skill only for agents intended to administer AVI/NSX ALB and AKO environments. <br>
Risk: Disabling TLS verification can hide controller impersonation or interception outside isolated labs. <br>
Mitigation: Keep TLS verification enabled in production and configure trusted CA certificates instead of using verify_ssl:false or curl -k. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-avi) <br>
- [Project homepage](https://github.com/vmware-skills/VMware-AVI) <br>
- [VMware AVI Capabilities](references/capabilities.md) <br>
- [VMware AVI Setup Guide](references/setup-guide.md) <br>
- [VMware AVI CLI Reference](references/cli-reference.md) <br>
- [Operating vmware-avi with a local / small model](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with CLI commands, operational summaries, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP tool results, diagnostics, and approval-gated operational recommendations] <br>

## Skill Version(s): <br>
1.8.9 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
