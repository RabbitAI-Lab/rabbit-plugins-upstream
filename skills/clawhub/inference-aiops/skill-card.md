## Description:

Inference AIops helps agents operate GPU inference clusters across vLLM, Ray Serve and Ray Jobs, SGLang, and TGI by gathering metrics, diagnosing latency and utilization issues, and proposing or executing governed scaling, deployment, model, LoRA, and cost actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and inference platform operators use this skill to inspect vLLM, Ray Serve, SGLang, and TGI serving environments, diagnose latency or utilization problems, and guide operational changes such as scaling, draining replicas, LoRA management, deployment lifecycle actions, and cost analysis. It is scoped to GPU inference serving rather than general infrastructure operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact write actions can affect production inference traffic when write-capable Ray or vLLM endpoints are reachable.

Mitigation: Prefer read-only network access by default and expose write-capable endpoints only when the operator intends the agent to perform production changes.

Risk: The skill does not provide an enforceable read-only mode or approval gate.

Mitigation: Scope authorization in the connected environment and require the agent or operator workflow to approve write operations before enabling write-capable access.

Risk: Credentials with broad access could allow unintended changes to the connected inference environment.

Mitigation: Use narrowly scoped credentials for the Ray and vLLM environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/inference-aiops)
- [Project homepage](https://github.com/AIops-tools/Inference-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cluster observations, ranked diagnoses, dry-run previews, audit annotations, and undo guidance.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
