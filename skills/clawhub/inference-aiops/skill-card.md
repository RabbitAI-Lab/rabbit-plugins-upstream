## Description:

Helps inference operators diagnose latency and GPU utilization, inspect serving health, and manage vLLM and Ray Serve deployments, with read-only observability for SGLang and TGI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Inference platform developers and operators use this skill to investigate serving bottlenecks, monitor GPU inference, and, with appropriate approval, adjust Ray Serve capacity and deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can interrupt serving or change production cluster behavior; MCP access does not enforce read-only mode or human approval.

Mitigation: Prefer read-only access for observation, restrict write-capable credentials, and require external human approval before high-risk writes.

Risk: Unauthenticated Ray or vLLM endpoints can expose high-impact cluster operations.

Mitigation: Require authentication or an authenticating proxy for inference and Ray endpoints.

Risk: Access to local credentials or the master password could expose operational secrets.

Mitigation: Protect ~/.inference-aiops/ and INFERENCE_AIOPS_MASTER_PASSWORD; use dry-run, audit, and undo as review and recovery aids, not authorization controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/inference-aiops)
- [Project homepage (skill metadata)](https://github.com/AIops-tools/Inference-AIops)
- [Capabilities](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples and diagnostic findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest or invoke operational actions against configured inference endpoints.]

## Skill Version(s):

0.12.0 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
