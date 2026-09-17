## Description:

Inference AIops helps agents operate GPU inference serving stacks across vLLM, Ray Serve, SGLang, and TGI with latency diagnosis, metrics inspection, scaling, drain, LoRA, model lifecycle, GPU utilization, Ray job, and cost-per-token workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and inference operations engineers use this skill to inspect, diagnose, and operate GPU inference clusters, especially vLLM/Ray Serve deployments and SGLang/TGI servers. It supports both read-only observability tasks and state-changing operations such as scaling, draining, LoRA changes, model lifecycle actions, and Ray job cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke disruptive cluster write actions through MCP without an enforced read-only mode or approval gate.

Mitigation: Limit network access and credentials to the intended inference endpoints, prefer read-only connectivity in production, and require operator change-control before write-capable sessions.

Risk: High-impact operations such as scale-to-zero, draining, restarts, undeploys, and model changes can interrupt or strand live traffic.

Mitigation: Use dry-run previews where available, verify current traffic and queue state first, and keep rollback or undo steps ready before executing changes.

Risk: Stored configuration and optional secrets under the inference-aiops state directory can grant access to inference targets.

Mitigation: Protect ~/.inference-aiops, INFERENCE_AIOPS_MASTER_PASSWORD, INFERENCE_AIOPS_CONFIG, and any legacy token environment variables with production credential controls.

## Reference(s):

- [Inference-AIops GitHub repository](https://github.com/AIops-tools/Inference-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and tool-call recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational recommendations, dry-run instructions, configuration steps, and risk-aware next actions for supported inference-serving targets.]

## Skill Version(s):

0.10.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
