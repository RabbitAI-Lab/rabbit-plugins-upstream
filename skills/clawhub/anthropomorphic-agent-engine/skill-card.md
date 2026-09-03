## Description:

Anthropomorphic psychology engine based on SPL Pure Core V8.0, enabling modular modeling of cognition, emotion, motivation, and social interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement

## Use Case:

Developers and agent builders use this skill to model deterministic persona state, emotion, motivation, relationship dynamics, language style, and safety-aware minor-protection behavior for long-running AI agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit and request logs may record persona, emotional, or safety-related state.

Mitigation: Set SPL_AUDIT_LOG=0 and SPL_LOG=0 for private or minor-related use unless a clear retention and access-control policy is in place.

Risk: Changing the HTTP bind address can expose the local chat API and browser UI beyond loopback.

Mitigation: Keep SPL_BIND on 127.0.0.1 unless a separate network-exposure review approves the deployment.

Risk: Optional LLM adapters or guardian callbacks can send input-derived prompts or high-risk snapshots to external services.

Mitigation: Enable OpenAI, Claude, chain adapters, or guardian callbacks only after explicit user or guardian consent, and minimize fields sent outside the local process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [ClawHub metadata homepage](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [Persona persistence reference](references/PersonaPersistence.md)
- [Emotion behavior map](references/EmotionBehaviorMap.md)
- [Motive conflict rules](references/MotiveConflictRules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deterministic engine usage guidance, persona-state descriptions, configuration notes, and safety integration guidance for agent workflows.]

## Skill Version(s):

2.4.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
