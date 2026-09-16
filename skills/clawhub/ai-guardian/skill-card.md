## Description:

AI Guardian helps agents observe and govern local LLM endpoints by inventorying models, scanning prompts, applying model policy to routed calls, detecting digest drift, and auditing observed usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security reviewers use this skill to inspect local LLM runtime state, identify unsanctioned or drifted models, scan prompts for sensitive content, and route selected prompts through policy checks before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs an external tool that server security evidence describes as unverifiable.

Mitigation: Pin or independently verify the installed ai-guardian package version before exposing it to an agent.

Risk: The skill exposes write-capable local model administration without built-in read-only or approval controls.

Mitigation: Use a restricted account or expose only observe and scan workflows unless model administration is intended.

Risk: Long-lived master passwords in plaintext environment variables can increase credential exposure.

Mitigation: Prefer interactive secret unlocking or short-lived, tightly scoped environment injection for non-interactive runs.

## Reference(s):

- [AI Guardian homepage](https://github.com/AIops-tools/AI-Guardian)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/ai-guardian)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run local ai-guardian CLI or MCP tools; route-through governance stores redacted findings rather than raw prompts.]

## Skill Version(s):

0.11.3 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
