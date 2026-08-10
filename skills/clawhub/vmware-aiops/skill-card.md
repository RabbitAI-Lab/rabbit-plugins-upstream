## Description: <br>
Manages VMware, vSphere, and ESXi VM lifecycle operations, deployments, guest operations, cluster changes, alarm handling, and investigation workflows for authorized infrastructure operators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to administer VMware environments through guided VM lifecycle, deployment, cluster, alarm, and investigation workflows. It is intended for authorized operators with scoped access to the target vCenter or ESXi systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can administer VMware infrastructure and includes write operations such as deletes, TTL auto-delete, guest execution, production data cloning, cluster changes, and alarm resets. <br>
Mitigation: Install only for authorized operators, use a dedicated least-privilege service account, label production targets, enforce deny rules for writes where appropriate, and require human review for high-impact operations. <br>
Risk: Webhook notifications can expose operational metadata if sent to an uncontrolled destination. <br>
Mitigation: Keep webhooks disabled unless the destination is controlled by the operator and limit payloads to aggregated alert metadata. <br>
Risk: Broad credentials or production access can expand the blast radius of agent mistakes. <br>
Mitigation: Scope vCenter or ESXi credentials to the minimum permissions required and prefer read-only companion skills for monitoring-only work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops) <br>
- [Project homepage](https://github.com/vmware-skills/VMware-AIops) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Investigation protocol](references/investigation-protocol.md) <br>
- [Setup guide](references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis] <br>
**Output Format:** [Markdown with inline shell commands and structured tool recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce MCP tool recommendations, CLI commands, remediation plans, and review prompts before infrastructure-changing actions.] <br>

## Skill Version(s): <br>
1.8.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
