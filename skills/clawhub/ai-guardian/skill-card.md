## Description:

ai-guardian helps agents audit and govern single-endpoint local LLM use with model inventory, policy checks, prompt scanning, route-through controls, usage logs, VRAM state, and provenance drift reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and local AI operators use this skill to inspect local model inventory, identify unsanctioned or drifted models, scan prompts for sensitive data or jailbreak patterns, and route approved prompts through guard controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise local model administration powers on the configured runtime.

Mitigation: Run it with an unprivileged or observe-only setup where possible, and expose write tools only when model lifecycle or policy changes are explicitly needed.

Risk: Installation and package identity controls are unclear in the security evidence.

Mitigation: Verify the package name, version, and publisher before installation, and pin the release used by the agent environment.

Risk: Proxy and non-Ollama support claims are unclear in the security evidence.

Mitigation: Treat non-Ollama and proxy workflows as requiring local validation until the publisher reconciles the documentation.

Risk: Route-through prompt governance only covers traffic that is actually sent through the guard.

Mitigation: Interpret usage logs as coverage of routed traffic, and do not treat an empty usage log as proof that direct runtime traffic did not occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/ai-guardian)
- [AI Guardian Source Repository](https://github.com/AIops-tools/AI-Guardian)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration snippets, and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the configured local LLM runtime and on which read or write tools the host exposes to the agent.]

## Skill Version(s):

0.11.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
