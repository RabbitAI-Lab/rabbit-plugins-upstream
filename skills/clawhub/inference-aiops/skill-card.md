## Description: <br>
Inference Aiops helps agents inspect and operate GPU inference serving clusters across vLLM, Ray Serve, SGLang, and TGI, including latency diagnosis, scaling, drain workflows, model operations, GPU utilization, Ray jobs, and cost-per-token estimates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to observe GPU inference clusters, diagnose latency or utilization problems, and perform governed operational changes such as scaling, draining replicas, managing LoRA adapters, and inspecting Ray jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform disruptive inference-cluster write operations and does not enforce a read-only mode or approval gate itself. <br>
Mitigation: Use observe-only network access when write authority is not intended, expose only metrics or read endpoints where possible, and require separate operator approval, least-privilege credentials, and a rollback plan before production write access. <br>
Risk: High-risk operations such as scale-to-zero, drain, restart, undeploy, redeploy, sleep, or LoRA unload can interrupt traffic or strand requests. <br>
Mitigation: Run dry-run previews first, verify current traffic and queue depth, confirm that remaining capacity can absorb load, and keep undo or restore steps ready before applying changes. <br>
Risk: Bearer tokens and INFERENCE_AIOPS_MASTER_PASSWORD can grant access to inference and Ray control-plane endpoints. <br>
Mitigation: Treat these values as secrets, avoid broad shell or CI exposure, prefer the encrypted secret store, and scope tokens to the minimum cluster permissions needed. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/AIops-tools/Inference-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run recommendations, audit annotations, measured cluster observations, and rollback steps for governed inference operations.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
