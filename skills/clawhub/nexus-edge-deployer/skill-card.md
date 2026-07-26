## Description: <br>
Deploys 1-bit quantized AI models on low-cost VPS infrastructure, with guidance for unit economics, Hetzner provisioning, Ollama or llama.cpp setup, and multi-tenant agent fleet management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shuwanito](https://clawhub.ai/user/shuwanito) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DevOps engineers use this skill to plan and operate edge AI deployments for Agent-as-a-Service, including model selection, VPS provisioning, local inference setup, monitoring, and cost analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live cloud infrastructure provisioning that may create billable VPS resources. <br>
Mitigation: Before any live Hetzner action, confirm the target account, API token scope, region, server size, monthly cost, exposed services, and rollback or deletion plan. <br>
Risk: Misconfigured inference endpoints could expose model services publicly. <br>
Mitigation: Authenticate inference endpoints and verify that public exposure is disabled unless explicitly intended and reviewed. <br>
Risk: 1-bit quantized models may not meet quality requirements for all production tasks. <br>
Mitigation: Benchmark model quality before production deployment and keep a higher-quality fallback path for critical workloads. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/shuwanito/skills/nexus-edge-deployer) <br>
- [NEXUS AI ROI calculator](https://shuwanito.github.io/nexus-ai/) <br>
- [NEXUS AI Corp GitHub profile](https://github.com/Shuwanito) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include deployment plans, cost calculations, monitoring guidance, and infrastructure safety checks.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
