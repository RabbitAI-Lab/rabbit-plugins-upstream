## Description:

Inference AIops helps agents operate GPU inference serving stacks across vLLM, Ray Serve, SGLang, and TGI for observability, latency root-cause analysis, scaling, model operations, and cost analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and inference platform operators use this skill to inspect GPU inference clusters, diagnose latency and utilization issues, and propose or run governed operational changes such as scaling, draining replicas, model operations, and cost analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform production-impacting inference operations and does not provide a built-in read-only mode or required approval gate.

Mitigation: Use read-only or network-restricted targets first, expose write-capable Ray or vLLM administrative endpoints only when intentional, and rely on environment permissions and agent policy to control write access.

Risk: High-risk operations such as scale-to-zero, drain, undeploy, redeploy, replica restart, LoRA unload, and sleep can strand or drop live traffic.

Mitigation: Run dry-run previews where available, confirm traffic and queue state before writes, require human authorization for disruptive actions, and use recorded undo descriptors for reversible changes.

Risk: The release depends on an external inference-aiops executable that the artifact does not pin or hash.

Mitigation: Verify the package provenance before installation and prefer isolated or controlled environments for production evaluation.

Risk: Bearer tokens and master password environment variables can expose access to inference and Ray endpoints if mishandled.

Mitigation: Prefer authenticated endpoints, protect INFERENCE_AIOPS_MASTER_PASSWORD and token variables, and use the encrypted secret store instead of legacy plaintext token environment variables.

## Reference(s):

- [Inference AIops ClawHub page](https://clawhub.ai/zw008/skills/inference-aiops)
- [Inference AIops homepage](https://github.com/AIops-tools/Inference-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and operational recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include risk-tiered operational advice, dry-run recommendations, audit context, and undo guidance for reversible changes.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
