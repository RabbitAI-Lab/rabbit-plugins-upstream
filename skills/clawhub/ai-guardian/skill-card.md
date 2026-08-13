## Description:

AI Guardian helps agents observe and govern single-endpoint local LLM runtimes by inventorying models, checking policy and provenance, scanning prompts, routing guarded generation, and auditing usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect local LLM endpoints, identify unsanctioned or drifted models, scan prompts for secrets, PII, code leakage, or jailbreak patterns, and route approved local generation through an audited guard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete local models and policy without a built-in read-only mode or approval gate.

Mitigation: Install it only where the agent account is allowed to manage the target local LLM runtime; for observe-only use, run against an account or runtime that cannot modify the model store, or expose only scan and observe tools.

Risk: Local ai-guardian state can include sensitive configuration, encrypted secrets, and observed usage records.

Mitigation: Treat ~/.ai-guardian as sensitive local state and avoid long-lived master passwords in environment variables that could be exposed through shell history, child processes, CI logs, or process inspection.

## Reference(s):

- [AI Guardian project homepage](https://github.com/AIops-tools/AI-Guardian)
- [ai-guardian capabilities](references/capabilities.md)
- [ai-guardian CLI reference](references/cli-reference.md)
- [ai-guardian setup and security guide](references/setup-guide.md)
- [Agent guardrails for ai-guardian](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command snippets and structured local-LLM governance recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local runtime state, local configuration paths, and audited guard decisions.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
