## Description:

Inference AIops helps agents operate GPU inference clusters across vLLM, Ray Serve, SGLang, and TGI by inspecting health and metrics, diagnosing latency or utilization issues, and guiding governed operational changes such as scaling, draining, LoRA operations, and deployment lifecycle actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and inference platform operators use this skill to monitor GPU inference services, diagnose latency or utilization problems, and perform controlled operational actions on vLLM/Ray Serve deployments or read-only checks for SGLang and TGI services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disruptive write controls can scale, drain, restart, unload, undeploy, or otherwise affect live inference service without an enforced read-only authorization gate.

Mitigation: Use the skill only against clusters where the agent is authorized to make operational changes, and restrict network/API access when an observe-only posture is required.

Risk: The release installs an external executable that security evidence describes as unpinned.

Mitigation: Pin the inference-aiops package to version 0.10.2 or another approved artifact before deployment.

Risk: Credentials and serving control-plane access can affect both Ray and inference endpoints.

Mitigation: Use separate least-privilege credentials, keep HTTPS certificate verification enabled where possible, and avoid plaintext token environment fallbacks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/inference-aiops)
- [Project homepage](https://github.com/AIops-tools/Inference-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, operational recommendations, and structured observations from tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations, audit guidance, risk-tier notes, and follow-up verification steps for inference operations.]

## Skill Version(s):

0.10.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
