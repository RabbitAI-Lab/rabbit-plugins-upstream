## Description:

ai-guardian helps agents observe and govern local LLM endpoints by inventorying models, checking policy and provenance, scanning prompts for secrets, PII, code, and jailbreak signals, and routing allowed prompts through guarded generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use ai-guardian to inspect local LLM runtimes, detect shadow or drifted models, scan prompts before they reach a model, and audit observed local LLM usage. It is aimed at single-endpoint local runtimes such as Ollama, llama.cpp, LM Studio, and local vLLM, not multi-node inference clusters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs external code that the security evidence describes as unpinned.

Mitigation: Install only from a pinned and trusted package source and review the release before installation.

Risk: Agent-exposed write tools can pull, unload, or delete local models without a built-in read-only or approval gate.

Mitigation: Prefer observe-only tool exposure or run against a runtime account that cannot administer the model store.

Risk: Unauthenticated or remotely reachable model endpoints can broaden access to local model operations.

Mitigation: Keep model endpoints local or otherwise authenticated and avoid exposing unauthenticated endpoints remotely.

Risk: Audit and observed-usage databases may contain sensitive operational records even when raw prompts are not stored.

Mitigation: Treat local ai-guardian state files as sensitive records and protect access to the user's home directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/ai-guardian)
- [Project homepage](https://github.com/AIops-tools/AI-Guardian)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with JSON tool results and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke MCP tools and local CLI commands against configured local LLM endpoints.]

## Skill Version(s):

0.11.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
