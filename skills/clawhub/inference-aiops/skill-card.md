## Description:

Inference AIops helps agents observe and operate GPU inference serving for vLLM, Ray Serve, SGLang, and TGI, including latency diagnosis, queue and KV-cache metrics, scaling, draining, model operations, Ray jobs, GPU utilization, and cost-per-token analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to triage and operate GPU inference clusters, especially vLLM and Ray Serve deployments with additional observability for SGLang and TGI. It supports latency root-cause analysis, scaling decisions, replica drains, model and adapter operations, Ray job inspection, and cost analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform disruptive live infrastructure changes, including scale-to-zero, replica drains, restarts, model sleep, adapter unloads, undeploys, and redeploys.

Mitigation: Run it under least privilege, restrict network access to approved inference and Ray endpoints, require a separate human approval process for production writes, and use dry-run previews where available.

Risk: The release installs external package code that may change if consumers do not pin the version.

Mitigation: Pin the package version to 0.10.1 or another reviewed release and scan updates before deployment.

Risk: Bearer tokens and the master password can expose control-plane access if mishandled.

Mitigation: Prefer authenticated endpoints, avoid long-lived exported master passwords, use the encrypted secret store, and run the skill from a least-privileged account.

Risk: Artifact documentation says live multi-GPU, thermal/throttle telemetry, and multi-node drain behavior have not been fully verified.

Mitigation: Validate behavior in a staging cluster before production use and treat unverified telemetry or drain scenarios as requiring operator review.

## Reference(s):

- [Inference AIops capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Project homepage](https://github.com/AIops-tools/Inference-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/inference-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool results with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational recommendations, dry-run guidance, audit context, and warnings for high-risk writes.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
