## Description:

AI Guardian helps agents observe and govern single-endpoint local LLM runtimes by inventorying models, checking policy and provenance, scanning prompts for secrets, PII, source code, and jailbreak patterns, routing guarded generation when configured, and reporting usage anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect local Ollama, llama.cpp, LM Studio, or single-node vLLM endpoints, detect unsanctioned or drifted models, scan prompts before model use, and audit guarded local LLM activity. It is intended for local endpoint governance rather than multi-node inference clusters or unrelated infrastructure operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive or policy-changing local model operations.

Mitigation: Run it with least privilege and expose only scan/read tools unless model deletion, model pulls, or policy changes are explicitly required.

Risk: Configured HTTP endpoints may expose local LLM control surfaces if reachable beyond the local host.

Mitigation: Keep endpoints loopback-only, or require HTTPS with verification before exposing them outside the trusted machine.

Risk: Audit, usage, undo, and secret files under ~/.ai-guardian contain sensitive operational data.

Mitigation: Restrict filesystem access to the governance state directory and handle those files as sensitive local security records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/ai-guardian)
- [Project homepage](https://github.com/AIops-tools/AI-Guardian)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and tool-selection recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local runtime observations, risk-band summaries, policy recommendations, and guarded workflow steps depending on available tools and endpoint state.]

## Skill Version(s):

0.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
